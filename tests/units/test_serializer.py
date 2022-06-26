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
import pytest
import json

def test_serializer():
    p = PackageDescription(
        "foo",
        [
            GroupOfPins(
                "G1",
                10,
                "Group 1",
                [
                    PinDescription("1", "D+", "I", "Non inverting input"),
                    PinDescription("2", "OUT", "O", "output"),
                    PinDescription("3", "D-", "I", "Inverting input"),
                ],
            ),
            GroupOfPins(
                "G2",
                20,
                "Group 2",
                [
                    PinDescription("6", "D0", "I", "Data bus"),
                    PinDescription("7", "D1", "O", "Data bus"),
                    PinDescription("8", "D4", "B", "Data bus"),
                    PinDescription("4", "D3", "I", "Data bus"),
                    PinDescription("5", "D2", "I", "Data bus"),
                ],
            ),
        ],
        [
            PinDescription("9", "VCC", "PWR", "Power supply"),
            PinDescription("10", "VCC", "PWR", "Power supply"),
            PinDescription("11", "GNDA", "GND", "Ground for analog part"),
            PinDescription("12", "VCCA", "PWR", "Power input for analog part"),
            PinDescription("13", "GND", "GND", "Ground"),
        ],
    )
    assert SerializerOfPackage().jsonFrom(p) == """{
  "meta": {
    "name": "foo",
    "aliases": [],
    "reference": "U",
    "datasheet": null,
    "footprint": null,
    "physical": "LayoutOfPins.DUAL_INLINE_PACKAGE"
  },
  "pins": [
    {
      "designator": "1",
      "name": "D+",
      "type": "I",
      "description": "Non inverting input",
      "group": "G1"
    },
    {
      "designator": "2",
      "name": "OUT",
      "type": "O",
      "description": "output",
      "group": "G1"
    },
    {
      "designator": "3",
      "name": "D-",
      "type": "I",
      "description": "Inverting input",
      "group": "G1"
    },
    {
      "designator": "4",
      "name": "D3",
      "type": "I",
      "description": "Data bus",
      "group": "G2"
    },
    {
      "designator": "5",
      "name": "D2",
      "type": "I",
      "description": "Data bus",
      "group": "G2"
    },
    {
      "designator": "6",
      "name": "D0",
      "type": "I",
      "description": "Data bus",
      "group": "G2"
    },
    {
      "designator": "7",
      "name": "D1",
      "type": "O",
      "description": "Data bus",
      "group": "G2"
    },
    {
      "designator": "8",
      "name": "D4",
      "type": "B",
      "description": "Data bus",
      "group": "G2"
    },
    {
      "designator": "9",
      "name": "VCC",
      "type": "PWR",
      "description": "Power supply"
    },
    {
      "designator": "10",
      "name": "VCC",
      "type": "PWR",
      "description": "Power supply"
    },
    {
      "designator": "11",
      "name": "GNDA",
      "type": "GND",
      "description": "Ground for analog part"
    },
    {
      "designator": "12",
      "name": "VCCA",
      "type": "PWR",
      "description": "Power input for analog part"
    },
    {
      "designator": "13",
      "name": "GND",
      "type": "GND",
      "description": "Ground"
    }
  ],
  "groups": [
    {
      "designator": "G1",
      "rank": 10,
      "comment": "Group 1",
      "pins": [
        "1",
        "2",
        "3"
      ]
    },
    {
      "designator": "G2",
      "rank": 20,
      "comment": "Group 2",
      "pins": [
        "4",
        "5",
        "6",
        "7",
        "8"
      ]
    }
  ]
}"""
