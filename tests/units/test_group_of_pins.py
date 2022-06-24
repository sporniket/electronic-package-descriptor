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

def compute_sequence_of_designators(pins:List[PinDescription]) -> str:
    """
    Returns a string of all the pins designators in order
    """
    return ' '.join([f"{p.designator.name_letter}{p.designator.name_number}" for p in pins])

def thenSublistShouldVerifyExpectations(sublist:List[PinDescription], length:int, sequence:str) -> None:
    assert(len(sublist) == length)
    assert(compute_sequence_of_designators(sublist) == sequence)

def test_that_GroupOfPins_recognizes_ampop_io():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','D+','I','Non inverting input'),
        PinDescription('2','OUT','O','output'),
        PinDescription('3','D-','I','Inverting input')
    ])
    assert(g.pattern == PatternOfGroup.AMPOP_IO)
    assert(g.directionnality == Directionnality.BI)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 3)
    assert(len(g.slots) == 2)
    thenSublistShouldVerifyExpectations(g.slots['in'], 2, '1 3')
    thenSublistShouldVerifyExpectations(g.slots['out'], 1, '2')

def test_that_GroupOfPins_recognizes_ampop_vref():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','VREF-','PWR','Negative voltage reference'),
        PinDescription('2','VREF+','PWR','Positive voltage reference')
    ])
    assert(g.pattern == PatternOfGroup.AMPOP_VREF)
    assert(g.directionnality == Directionnality.IN)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 2)
    assert(len(g.slots) == 1)
    thenSublistShouldVerifyExpectations(g.slots['in'], 2, '2 1')

def test_that_GroupOfPins_recognizes_power():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','VCC','PWR','Power supply'),
        PinDescription('2','VCC','PWR','Power supply'),
        PinDescription('3','GNDA','GND','Ground for analog part'),
        PinDescription('4','VCCA','PWR','Power input for analog part'),
        PinDescription('5','GND','GND','Ground')
    ])
    assert(g.pattern == PatternOfGroup.POWER)
    assert(g.directionnality == Directionnality.BI)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 5)
    assert(len(g.slots) == 2)
    thenSublistShouldVerifyExpectations(g.slots['in'], 3, '1 2 4')
    thenSublistShouldVerifyExpectations(g.slots['out'], 2, '3 5')

def test_that_GroupOfPins_recognizes_bus():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','D0','I','Data bus'),
        PinDescription('2','D1','O','Data bus'),
        PinDescription('3','D4','B','Data bus'),
        PinDescription('4','D3','I','Data bus'),
        PinDescription('5','D2','I','Data bus')
    ])
    assert(g.pattern == PatternOfGroup.BUS)
    assert(g.directionnality == Directionnality.BI)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 5)
    assert(len(g.slots) == 4)
    thenSublistShouldVerifyExpectations(g.slots['in'], 3, '1 4 5')
    thenSublistShouldVerifyExpectations(g.slots['out'], 1, '2')
    thenSublistShouldVerifyExpectations(g.slots['bi'], 1, '3')
    thenSublistShouldVerifyExpectations(g.slots['bus'], 5, '3 4 5 2 1')

def test_that_GroupOfPins_recognizes_nothing():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','AS','O','Data bus'),
        PinDescription('2','DS','O','Data bus'),
        PinDescription('3','DTACK','I','Data bus'),
        PinDescription('4','R/W','B','Data bus'),
        PinDescription('5','TEST','DNC','Test pin'),
    ])
    assert(g.pattern == None)
    assert(g.directionnality == Directionnality.BI)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 5)
    assert(len(g.slots) == 4)
    thenSublistShouldVerifyExpectations(g.slots['in'], 1, '3')
    thenSublistShouldVerifyExpectations(g.slots['out'], 2, '1 2')
    thenSublistShouldVerifyExpectations(g.slots['bi'], 1, '4')
    thenSublistShouldVerifyExpectations(g.slots['others'], 1, '5')
