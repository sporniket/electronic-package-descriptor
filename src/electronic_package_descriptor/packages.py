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
from typing import List, Optional
from .commons import Directionnality
from .pins import PinDescription
from .groups_of_pins import GroupOfPins


class LayoutOfPins(Enum):
    """
    A list of supported pin layout rendering.

    DIP, LCC and QFP are taken after the actual package series.

    BRD is for little development modules that tend to have a DIP format, but with the 2 halves of pins numbered from
    top to bottom, e.g. for a 40 pins module : the pins of the left side will be numbered 1 to 20 from top to bottom,
    and the pins of the rigth side will be numbered 21 to 40 from top to bottom ; whereas a DIP package will have the
    pins of the left side numbered 1 to 20 from top to bottom, and the pins of the right side numbered 40 downto 21 from
    top to bottom.
    """

    DUAL_INLINE_PACKAGE = "DIP"
    BOARD_DUAL = "BRD"
    LEADED_CHIP_CARRIER = "LCC"
    QUAD_FLAT_PACKAGE = "QFP"
    DUAL_INLINE_MODULE = "DIM"
    SINGLE_INLINE_MODULE = "SIM"


class PackageDescription:
    """
    A bunch of pins (some grouped, some ungrouped), and some metadata to describe an electronic package.

    Default metadata assume a DIP integrated circuit (reference prefix is 'U') without alias nor footprint designator.
    """

    def __init__(
        self,
        name: str,
        groupedPins: List[GroupOfPins],
        ungroupedPins: List[PinDescription],
        *,
        layoutOfPins: LayoutOfPins = LayoutOfPins.DUAL_INLINE_PACKAGE,
        prefix: str = "U",
        datasheet: str = None,
        footprintDesignator: Optional[str] = None,
        aliases: Optional[List[str]] = None
    ):
        self.name = name
        self.groupedPins = groupedPins
        self.ungroupedPins = ungroupedPins
        self.layoutOfPins = layoutOfPins
        self.prefix = prefix
        self.datasheet = datasheet
        self.footprintDesignator = footprintDesignator
        self.aliases = () if aliases == None else tuple(aliases)
