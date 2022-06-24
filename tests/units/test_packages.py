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
import pytest

def test_default_values():
    p = PackageDescription('foo', [], [])
    assert(p.name == 'foo')
    assert(len(p.groupedPins) == 0)
    assert(len(p.ungroupedPins) == 0)
    assert(p.layoutOfPins == LayoutOfPins.DUAL_INLINE_PACKAGE)
    assert(p.prefix == 'U')
    assert(p.footprintDesignator == None)
    assert(p.aliases == ())
