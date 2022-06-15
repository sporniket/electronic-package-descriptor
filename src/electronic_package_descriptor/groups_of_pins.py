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

def PatternOfGroup(Enum):
    """
    The pins of a groups are analysed to assess one of the recognized pattern.
    """
    REGULAR = 0 # the default, a bunch on ins, outs and bidirectionnal pins.
    BUS = 1 # the whole group is a bus, ex (ADDR[0..15])
    AMPOP = 2 # Exactly one differential pair and one output
    POWER = 3 # A bunch of power inputs and grounds
    POWER_AMPOP = 4 # Exactly one differential pair of power input, and optionnal grounds
