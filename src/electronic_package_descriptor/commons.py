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
from enum import IntEnum


class Directionnality(IntEnum):
    """
    For a connected pin, tells about how the signal is either an input, output, or bidirectionnal signal ; as a side
    feature, one can add the int value to the rank to sort the pins grouped by directionnality.

    For a group of pins, tells whether there are pins to render on the input side only, on the output side only, or both
    sides.
    """

    IN = 0
    OUT = 1000
    BI = 2000
