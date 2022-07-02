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


class DeserializerOfPackage:
    def packageFromJsonString(self, src) -> PackageDescription:
        """
        Deserialize a package from a JSON source compatible with ``json.loads()`` (i.e. a ``str``, ``bytes`` or
        ``bytearray`` instance containing a JSON document).
        """
        return self.packageFromIntermediateTree(json.loads(src))

    def packageFromIntermediateTree(self, tree: dict):
        """
        Instanciate a package from the tree structure that can be obtained by loading a JSON source.
        """
        # step 1 : process pins
        pins = [
            PinDescription(p["designator"], p["name"], p["type"], p["description"])
            for p in tree["pins"]
        ]
        # step 2 : process groups
        groups = [
            GroupOfPins(
                g["designator"],
                g["rank"],
                g["comment"],
                [p for p in pins if p.designator.fullname in g["pins"]],
            )
            for g in tree["groups"]
        ]
        groupedPins = []
        for g in groups:
            groupedPins += g.pins
        ungroupedPins = [p for p in pins if p not in groupedPins]
        # step 3 : process package
        meta = tree["meta"]
        return PackageDescription(
            meta["name"],
            groups,
            ungroupedPins,
            layoutOfPins=LayoutOfPins(meta["physical"]),
            prefix=meta["reference"],
            datasheet=meta["datasheet"],
            footprintDesignator=meta["footprint"],
            aliases=meta["aliases"],
        )
