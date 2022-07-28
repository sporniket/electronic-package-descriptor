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
from typing import Optional
import json


class SerializerOfPackage:
    def __init__(self, *, indent: int = 2):
        self.indent = indent

    def __convertPin(
        self, pin: PinDescription, groupName: Optional[str] = None
    ) -> dict:
        result = {
            "designator": pin.designator.fullname,
            "name": pin.name,
            "type": pin.type.value,
            "description": pin.description,
        }
        if groupName != None:
            result["group"] = groupName
        return result

    def __convertGroup(self, group: GroupOfPins) -> dict:
        return {
            "pins": [self.__convertPin(p, group.designator) for p in group.pins],
            "group": {
                "designator": group.designator,
                "rank": group.rank,
                "comment": group.comment,
                "pins": sorted(
                    [p.designator.fullname for p in group.pins],
                    key=lambda p: PinDesignator(p).rank,
                ),
            },
        }

    def __convertPackage(self, package: PackageDescription) -> dict:
        pins = [self.__convertPin(p) for p in package.ungroupedPins]
        groups = []
        for g in package.groupedPins:
            gg = self.__convertGroup(g)
            pins.extend(gg["pins"])
            groups.append(gg["group"])
        return {
            "meta": {
                "name": package.name,
                "aliases": package.aliases,
                "reference": package.prefix,
                "datasheet": package.datasheet,
                "footprint": package.footprintDesignator,
                "physical": package.layoutOfPins.value,
            },
            "pins": sorted(pins, key=lambda p: PinDesignator(p["designator"]).rank),
            "groups": sorted(groups, key=lambda g: g["rank"]),
        }

    def jsonFrom(self, package: PackageDescription) -> str:
        return json.dumps(self.__convertPackage(package), indent=self.indent, ensure_ascii=False)
