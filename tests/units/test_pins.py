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


def test_PinDesignator():
    with pytest.raises(SyntaxError):
        pdes = PinDesignator("totally wrong")

    pdes = PinDesignator("C12")
    assert pdes.type == TypeOfPinDesignator.LETTER_NUMBER
    assert pdes.name_letter == "C"
    assert pdes.name_number == 12
    assert pdes.rank == 64
    assert pdes.row == 3
    assert pdes.column == 12

    pdes = PinDesignator("48")
    assert pdes.type == TypeOfPinDesignator.NUMBER
    assert pdes.name_letter == ""
    assert pdes.name_number == 48
    assert pdes.rank == 48
    assert pdes.row == 48
    assert pdes.column == 48


def test_PinDimensions():
    dim = PinDimensions("whatever")
    assert dim.thickness == 1
    assert dim.spanning == 8


def test_PinDescription():
    pds = PinDescription("C5", "CLK", "ICLK", "Main clock")
    assert pds.type == TypeOfPin.INPUT_CLOCK
    assert pds.directionnality == Directionnality.IN
    assert pds.name == "CLK"
    assert pds.bus == None
    assert pds.pair == None
    assert pds.description == "Main clock"


def test_ElementOfPair():
    e = ElementOfPair.of("VREF+")
    assert e.polarity == PolarityOfPairElement.PLUS
    assert e.rank == 0
    assert e.prefix == "VREF"
    e = ElementOfPair.of("VREFP")
    assert e.polarity == PolarityOfPairElement.PLUS
    assert e.rank == 0
    assert e.prefix == "VREF"
    e = ElementOfPair.of("VREF-")
    assert e.polarity == PolarityOfPairElement.MINUS
    assert e.rank == 1
    assert e.prefix == "VREF"
    e = ElementOfPair.of("VREFM")
    assert e.polarity == PolarityOfPairElement.MINUS
    assert e.rank == 1
    assert e.prefix == "VREF"
    e = ElementOfPair.of("whatever")
    assert e == None


def test_ElementOfBus():
    e = ElementOfBus.of("CLK0.5")
    assert e.rank == 0.5
    assert e.prefix == "CLK"
    e = ElementOfBus.of("D15")
    assert e.rank == 15.0
    assert e.prefix == "D"
    e = ElementOfBus.of("whatever")
    assert e == None


def test_Directionnality():
    assert (
        PinDescription("C5", "CLK", "PWR", "Main clock").directionnality
        == Directionnality.IN
    )
    assert (
        PinDescription("C5", "CLK", "GND", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert PinDescription("C5", "CLK", "DNC", "Main clock").directionnality == None
    assert (
        PinDescription("C5", "CLK", "I", "Main clock").directionnality
        == Directionnality.IN
    )
    assert (
        PinDescription("C5", "CLK", "ICLK", "Main clock").directionnality
        == Directionnality.IN
    )
    assert (
        PinDescription("C5", "CLK", "O", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "OCLK", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "O3", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "OCOL", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "OEMT", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "OPSV", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "OPWR", "Main clock").directionnality
        == Directionnality.OUT
    )
    assert (
        PinDescription("C5", "CLK", "B3", "Main clock").directionnality
        == Directionnality.BI
    )
    assert (
        PinDescription("C5", "CLK", "B", "Main clock").directionnality
        == Directionnality.BI
    )
