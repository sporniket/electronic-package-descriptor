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


def assert_that_group_is_as_expected(
    g: GroupOfPins, designator: str, rank: int, comment: str, pins: str
):
    assert g.designator == designator
    assert g.rank == rank
    assert g.comment == comment
    pinsDesgns = " ".join([p.designator.fullname for p in g.pins])
    assert pinsDesgns == pins


def test_deserializer():
    p = DeserializerOfPackage().packageFromJsonString(
        """{
  "meta": {
    "name": "foo",
    "aliases": [],
    "reference": "U",
    "datasheet": null,
    "footprint": null,
    "physical": "DIP"
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
    )
    assert p.name == "foo"
    assert p.prefix == "U"
    assert p.datasheet == None
    assert len(p.aliases) == 0
    assert p.footprintDesignator == None
    assert p.layoutOfPins == LayoutOfPins.DUAL_INLINE_PACKAGE
    assert len(p.ungroupedPins) == 5
    assert len(p.groupedPins) == 2
    assert_that_group_is_as_expected(p.groupedPins[0], "G1", 10, "Group 1", "1 2 3")
    assert_that_group_is_as_expected(p.groupedPins[1], "G2", 20, "Group 2", "4 5 6 7 8")
    assert (
        " ".join([pn.designator.fullname for pn in p.ungroupedPins]) == "9 10 11 12 13"
    )


def test_deserializer_supports_missing_optionnal_fields():
    p = DeserializerOfPackage().packageFromJsonString(
        """{
  "meta": {
    "name": "foo"
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
    )
    assert p.name == "foo"
    assert p.prefix == "U"
    assert p.datasheet == None
    assert len(p.aliases) == 0
    assert p.footprintDesignator == None
    assert p.layoutOfPins == LayoutOfPins.DUAL_INLINE_PACKAGE
    assert len(p.ungroupedPins) == 5
    assert len(p.groupedPins) == 2
    assert_that_group_is_as_expected(p.groupedPins[0], "G1", 10, "Group 1", "1 2 3")
    assert_that_group_is_as_expected(p.groupedPins[1], "G2", 20, "Group 2", "4 5 6 7 8")
    assert (
        " ".join([pn.designator.fullname for pn in p.ungroupedPins]) == "9 10 11 12 13"
    )
