"""
---
(c) 2022 David SPORN
---
This file is part of Electronic Package Descriptor.
Electronic Package Descriptor is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Electronic Package Descriptor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Electronic Package Descriptor.
If not, see <https://www.gnu.org/licenses/>. 
---
"""
from electronic_package_descriptor import *
from typing import List
import re


class ContextOfParsing:
    def __init__(self):
        self.meta = {
            "aliases": [],
            "reference": "U",
            "physical": LayoutOfPins.DUAL_INLINE_PACKAGE.value,
        }
        self.pins = []
        self.groups = []


def stripAll(stringList: List[str]) -> List[str]:
    """
    Returns the given list of strings, with each item stripped from leading and trailing spaces.
    """
    return list(map(lambda s: s.strip(), stringList))


def formatSignalName(name: str) -> str:
    """
    Format a single signal name
    """
    if name.startswith("/"):
        return "~" + name[1:] + "~"
    return name


def formatSignalNames(ssvNames: str) -> str:
    """
    Format a list of signal names (space separated values).

    Each name is individually formatted using ``formatSignalName(name)``, then joined with a ``/``.
    """
    names = ssvNames.split(" ")
    return "/".join(
        map(lambda n: formatSignalName(n), filter(lambda n: len(n) > 0, names))
    )


class LineHandler:
    """
    The datasheet is parsed line by line by a finite state machine.

    A line handler parse a given line, update the context and return the next state index.
    """

    def handle(self, context, line: str, state: int) -> int:
        """
        Returns the next state index, after having parsed the given line and updated the context.
        By default, do nothing.
        """
        return state


class LineHandlerForHeader(LineHandler):
    def __init__(self):
        self.reDefineAliases = re.compile("^aliases[ ]*\:.*", re.I)
        self.reDefineReference = re.compile("^reference[ ]*\:.*", re.I)
        self.reDefineDatasheet = re.compile("^datasheet[ ]*\:.*", re.I)
        self.reDefineFootprint = re.compile("^footprint[ ]*\:.*", re.I)
        self.reDefinePhysical = re.compile("^pins[ ]+layout[ ]*\:.*", re.I)
        self.reSectionPinout = re.compile("^pinout", re.I)

    def normalizeMetaName(self, name:str)->str:
        norm = re.sub(r"[ ()_,/]+", "_", name)
        if norm[0] == "_":
            norm = norm[1:]
        if norm[-1] == "_":
            norm = norm[:-1]
        return norm

    def handle(self, context, line: str, state: int) -> int:
        if line.startswith("# "):
            context.meta["name"] = self.normalizeMetaName(line[2:].strip().upper())
            return state
        if line.startswith("> "):
            return state
        if line.startswith("* "):
            line = line[2:].strip()
            if self.reDefineAliases.match(line):
                context.meta["aliases"] = stripAll(line.split(":", 1)[1].split(","))
                return state
            if self.reDefineReference.match(line):
                context.meta["reference"] = line.split(":", 1)[1].strip()
                return state
            if self.reDefineDatasheet.match(line):
                context.meta["datasheet"] = line.split(":", 1)[1].strip()
                return state
            if self.reDefineFootprint.match(line):
                context.meta["footprint"] = line.split(":", 1)[1].strip()
                return state
            if self.reDefinePhysical.match(line):
                context.meta["physical"] = line.split(":", 1)[1].strip()
                return state
        if line.startswith("## "):
            line = line[3:].strip()
            if self.reSectionPinout.match(line):
                return state + 1
        return state


class LineHandlerWaitingForStartOfTableData(LineHandler):
    def __init__(self):
        self.reTableHeadMark = re.compile("^\|[-]{3,}\|.*")

    def handle(self, context, line: str, state: int) -> int:
        if self.reTableHeadMark.match(line):
            return state + 1
        return state


class LineHandlerForPinoutData(LineHandler):
    def __init__(self):
        pass

    def handle(self, context, line: str, state: int) -> int:
        if len(line) == 0:
            return state + 1
        fields = stripAll(line.split("|"))
        if len(fields) >= 6:
            pin = {
                "designator": fields[1],
                "name": formatSignalNames(fields[2]),
                "type": fields[3].replace("?", "").upper(),
                "group": fields[4].upper(),
                "description": fields[5],
            }
            context.pins.append(pin)
        return state


class LineHandlerWaitingForEndOfPinoutSection(LineHandler):
    def __init__(self):
        self.reSectionPinGroup = re.compile("^pin groups", re.I)

    def handle(self, context, line: str, state: int) -> int:
        if line.startswith("### "):
            line = line[4:]
            if self.reSectionPinGroup.match(line):
                return state + 1
        return state


class LineHandlerForPinGroupData(LineHandler):
    def __init__(self):
        pass

    def handle(self, context, line: str, state: int) -> int:
        if len(line) == 0:
            return state + 1
        fields = stripAll(line.split("|"))
        if len(fields) >= 4:
            group = {
                "designator": fields[1],
                "rank": int(fields[2]),
                "comment": fields[3],
            }
            context.groups.append(group)
        return state


class ListenerOfParserEvent:
    """
    Third party scripts can be notified for parser events to monitor the parsing.
    """

    def onProcessingNextLine(self, index: int, line: str):
        """
        Called before processing the given line (index and content)
        """
        pass

    def onDoneProcessingLine(self):
        """
        Called after having succesfully processed the line
        """
        pass

    def onPostProcessing(self):
        """
        All the line have been succesfully processed.
        """
        pass

    def onDone(self):
        """
        The parser is about to return the package.
        """
        pass


class ParserOfMarkdownDatasheet:
    def __init__(self):
        self.handlers = [
            LineHandlerForHeader(),
            LineHandlerWaitingForStartOfTableData(),
            LineHandlerForPinoutData(),
            LineHandlerWaitingForEndOfPinoutSection(),
            LineHandlerWaitingForStartOfTableData(),
            LineHandlerForPinGroupData(),
            LineHandler(),
        ]
        self.listeners = []
        self.deserializer = DeserializerOfPackage()

    def addListener(self, listener: ListenerOfParserEvent):
        """
        Register a listener, returns this parser to chain calls
        """
        self.listeners.append(listener)
        return self

    def notifyNextLine(self, index: int, line: str):
        for l in self.listeners:
            l.onProcessingNextLine(index, line)

    def notifyDoneLine(self):
        for l in self.listeners:
            l.onDoneProcessingLine()

    def notifyDoneLines(self):
        for l in self.listeners:
            l.onPostProcessing()

    def notifyDone(self):
        for l in self.listeners:
            l.onDone()

    def parseLines(self, src: List[str]) -> PackageDescription:
        count = 0
        state = 0
        context = ContextOfParsing()
        for line in src:
            self.notifyNextLine(count, line)
            # Strips the newline character
            line = line.strip()
            state = self.handlers[state].handle(context, line, state)
            count += 1
            self.notifyDoneLine()
        self.notifyDoneLines()
        for g in context.groups:
            g["pins"] = [
                p["designator"] for p in context.pins if p["group"] == g["designator"]
            ]
        p = self.deserializer.packageFromIntermediateTree(
            {"meta": context.meta, "pins": context.pins, "groups": context.groups}
        )
        self.notifyDone()
        return p
