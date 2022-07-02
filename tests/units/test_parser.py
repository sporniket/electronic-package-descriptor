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


def test_parser():
    srcLines = """# 74x04 Hex Inverter

    > This datasheet is marked with CC0 1.0
    > Universal. To view a copy of this license, visit
    > http://creativecommons.org/publicdomain/zero/1.0

    ## Symbol

    * Aliases : 7404,74LS04
    * Reference : U
    * Datasheet : https://www.ti.com/lit/ds/symlink/sn74ls04.pdf
    * Footprint : Package_DIP:DIP-14_W7.62mm_LongPads

    ## Pinout

    |Pin|Name|Pin Type|Group|Comment|
    |---|---|---|---|---|
    |1|1A|I|1|Signal to invert|
    |2|1Y|O|1|Inverted signal|
    |3|2A|I|2|Signal to invert|
    |4|2Y|O|2|Inverted signal|
    |5|3A|I|3|Signal to invert|
    |6|3Y|O|3|Inverted signal|
    |7|GND|GND|||
    |8|4Y|O|4|Inverted signal|
    |9|4A|I|4|Signal to invert|
    |10|5Y|O|5|Inverted signal|
    |11|5A|I|5|Signal to invert|
    |12|6Y|O|6|Inverted signal|
    |13|6A|I|6|Signal to invert|
    |14|Vcc|PWR|||

    ### Pin groups

    |Group id|Rank|Comment|
    |---|---|---|
    |1|10|Inverter #1|
    |2|20|Inverter #2|
    |3|30|Inverter #3|
    |4|40|Inverter #4|
    |5|50|Inverter #5|
    |6|60|Inverter #6|
""".splitlines()
    p = ParserOfMarkdownDatasheet().parseLines(srcLines)
    assert (
        SerializerOfPackage().jsonFrom(p)
        == """{
  "meta": {
    "name": "74x04_Hex_Inverter",
    "aliases": [
      "7404",
      "74LS04"
    ],
    "reference": "U",
    "datasheet": "https://www.ti.com/lit/ds/symlink/sn74ls04.pdf",
    "footprint": "Package_DIP:DIP-14_W7.62mm_LongPads",
    "physical": "DIP"
  },
  "pins": [
    {
      "designator": "1",
      "name": "1A",
      "type": "I",
      "description": "Signal to invert",
      "group": "1"
    },
    {
      "designator": "2",
      "name": "1Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "1"
    },
    {
      "designator": "3",
      "name": "2A",
      "type": "I",
      "description": "Signal to invert",
      "group": "2"
    },
    {
      "designator": "4",
      "name": "2Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "2"
    },
    {
      "designator": "5",
      "name": "3A",
      "type": "I",
      "description": "Signal to invert",
      "group": "3"
    },
    {
      "designator": "6",
      "name": "3Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "3"
    },
    {
      "designator": "7",
      "name": "GND",
      "type": "GND",
      "description": ""
    },
    {
      "designator": "8",
      "name": "4Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "4"
    },
    {
      "designator": "9",
      "name": "4A",
      "type": "I",
      "description": "Signal to invert",
      "group": "4"
    },
    {
      "designator": "10",
      "name": "5Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "5"
    },
    {
      "designator": "11",
      "name": "5A",
      "type": "I",
      "description": "Signal to invert",
      "group": "5"
    },
    {
      "designator": "12",
      "name": "6Y",
      "type": "O",
      "description": "Inverted signal",
      "group": "6"
    },
    {
      "designator": "13",
      "name": "6A",
      "type": "I",
      "description": "Signal to invert",
      "group": "6"
    },
    {
      "designator": "14",
      "name": "VCC",
      "type": "PWR",
      "description": ""
    }
  ],
  "groups": [
    {
      "designator": "1",
      "rank": 10,
      "comment": "Inverter #1",
      "pins": [
        "1",
        "2"
      ]
    },
    {
      "designator": "2",
      "rank": 20,
      "comment": "Inverter #2",
      "pins": [
        "3",
        "4"
      ]
    },
    {
      "designator": "3",
      "rank": 30,
      "comment": "Inverter #3",
      "pins": [
        "5",
        "6"
      ]
    },
    {
      "designator": "4",
      "rank": 40,
      "comment": "Inverter #4",
      "pins": [
        "8",
        "9"
      ]
    },
    {
      "designator": "5",
      "rank": 50,
      "comment": "Inverter #5",
      "pins": [
        "10",
        "11"
      ]
    },
    {
      "designator": "6",
      "rank": 60,
      "comment": "Inverter #6",
      "pins": [
        "12",
        "13"
      ]
    }
  ]
}"""
    )
