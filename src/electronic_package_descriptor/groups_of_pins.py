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
from enum import Enum
from typing import List
from .commons import Directionnality
from .pins import PinDescription, PolarityOfPairElement, TypeOfPin


class PatternOfGroup(Enum):
    """
    The pins of a groups are analysed to assess one of the recognized pattern.
    """

    BUS = 1  # All the pins are in a single bus
    POWER = 2  # Only power pins and grounds
    AMPOP_IO = 3  # A pair of inputs + 1 output
    AMPOP_VREF = 4  # Only power pins and grounds


def _checkPolarity(group: List[PinDescription]):
    """
    Checks that the list of pins (that are element of the same pair) contains all the polarities.
    """
    hasPlus = False
    hasMinus = False
    for p in group:
        if p.pair != None:
            if hasPlus == False and p.pair.polarity == PolarityOfPairElement.PLUS:
                hasPlus = True
                if hasMinus == True:
                    return True
            elif hasMinus == False and p.pair.polarity == PolarityOfPairElement.MINUS:
                hasMinus = True
                if hasPlus == True:
                    return True
    return False


def _checkPowerPair(group):
    """
    Checks that the list of pins (that are element of the same pair) are only of type power.
    """
    for p in group:
        if p.type != TypeOfPin.POWER:
            return False
    return True


def _checkInputPair(group):
    """
    Checks that the list of pins (that are element of the same pair) are only of type input.
    """
    for p in group:
        if p.type != TypeOfPin.INPUT:
            return False
    return True


def _findFirstOutput(group):
    """
    Find the first pin having the OUT directionnality
    """
    for p in group:
        if p.directionnality == Directionnality.OUT:
            return p
    return None


def _checkPowerGroup(group):
    """
    Checks that all the pins of the group are power inputs or ground.
    """
    for p in group:
        if p.type != TypeOfPin.POWER and p.type != TypeOfPin.GROUND:
            return False
    return True


def _fillSlots(pins: List[PinDescription]):
    slots = {"in": [], "out": [], "bi": [], "others": []}
    for p in pins:
        if p.directionnality == Directionnality.IN:
            slots["in"].append(p)
        elif p.directionnality == Directionnality.OUT:
            slots["out"].append(p)
        elif p.directionnality == Directionnality.BI:
            slots["bi"].append(p)
        else:
            slots["others"].append(p)
    return {k: v for k, v in slots.items() if len(v) > 0}


class GroupOfPins:
    def __init__(
        self, designator: str, rank: int, comment: str, pins: List[PinDescription]
    ):
        self.designator = designator
        self.rank = rank
        self.comment = comment
        self.pins = pins
        self.pattern = None
        self.slots = _fillSlots(pins)  # default shuffle
        self.directionnality = None
        if "in" in self.slots:
            if "out" not in self.slots and "bi" not in self.slots:
                self.directionnality = Directionnality.IN
            else:
                self.directionnality = Directionnality.BI
        else:
            if "out" in self.slots or "bi" in self.slots:
                self.directionnality = Directionnality.OUT

        # Pass 1 : scan the pins and regroup by bus or pair
        buses = {}
        pairs = {}
        for pin in pins:
            if pin.bus != None:
                if pin.bus.prefix in buses:
                    buses[pin.bus.prefix].append(pin)
                else:
                    buses[pin.bus.prefix] = [pin]
            if pin.pair != None:
                if pin.pair.prefix in pairs:
                    pairs[pin.pair.prefix].append(pin)
                else:
                    pairs[pin.pair.prefix] = [pin]

        # Pass 2 : weed out degenerated buses (length = 1) and pairs (only one polarity)
        buses = {k: v for (k, v) in buses.items() if len(v) > 1}
        pairs = {k: v for (k, v) in pairs.items() if len(v) > 1 and _checkPolarity(v)}

        # Pass 3 : recognize patterns.
        countOfPairs = len(pairs)
        countOfBuses = len(buses)
        if countOfBuses + countOfPairs > 0:
            if countOfBuses == 1 and countOfPairs == 0:
                self.pattern = PatternOfGroup.BUS
                self.slots = {"bus": sorted(
                    self.pins, key=lambda p: p.bus.rank, reverse=True
                )}
                self.directionnality = self.slots["bus"][0].directionnality
                return
            elif countOfBuses == 0 and countOfPairs > 0:
                if countOfPairs == 1:
                    thePair = pairs[next(iter(pairs))]
                    if len(self.pins) == len(thePair) and _checkPowerPair(thePair):
                        self.pattern = PatternOfGroup.AMPOP_VREF
                        self.slots = {"in": sorted(thePair, key=lambda p: p.pair.rank)}
                        return
                    elif len(self.pins) == len(thePair) + 1:
                        theOutput = _findFirstOutput(self.pins)
                        if theOutput != None and _checkInputPair(thePair):
                            self.pattern = PatternOfGroup.AMPOP_IO
                            self.slots = {
                                "in": sorted(thePair, key=lambda p: p.pair.rank),
                                "out": [theOutput],
                            }
                            return
        else:
            if _checkPowerGroup(self.pins) == True:
                self.pattern = PatternOfGroup.POWER
                return
