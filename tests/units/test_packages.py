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
