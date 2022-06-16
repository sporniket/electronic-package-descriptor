from electronic_package_descriptor import *
import pytest

def test_PinDesignator():
    with pytest.raises(SyntaxError):
        pdes = PinDesignator('totally wrong')

    pdes = PinDesignator('C12')
    assert(pdes.type == TypeOfPinDesignator.LETTER_NUMBER)
    assert(pdes.name_letter == 'C')
    assert(pdes.name_number == 12)
    assert(pdes.rank == 64)
    assert(pdes.row == 3)
    assert(pdes.column == 12)

    pdes = PinDesignator('48')
    assert(pdes.type == TypeOfPinDesignator.NUMBER)
    assert(pdes.name_letter == '')
    assert(pdes.name_number == 48)
    assert(pdes.rank == 48)
    assert(pdes.row == 48)
    assert(pdes.column == 48)

def test_PinDimensions():
    dim = PinDimensions('whatever')
    assert(dim.thickness == 1)
    assert(dim.spanning == 8)

def test_PinDescription():
    pds = PinDescription('C5','CLK','ICLK','Main clock')
    assert(pds.type == TypeOfPin.INPUT_CLOCK)
    assert(pds.name == 'CLK')
    assert(pds.bus == None)
    assert(pds.pair == None)
    assert(pds.description == 'Main clock')

def test_ElementOfPair():
    e = ElementOfPair.of('VREF+')
    assert(e.polarity == PolarityOfPairElement.PLUS)
    assert(e.rank == 0)
    assert(e.prefix == 'VREF')
    e = ElementOfPair.of('VREFP')
    assert(e.polarity == PolarityOfPairElement.PLUS)
    assert(e.rank == 0)
    assert(e.prefix == 'VREF')
    e = ElementOfPair.of('VREF-')
    assert(e.polarity == PolarityOfPairElement.MINUS)
    assert(e.rank == 1)
    assert(e.prefix == 'VREF')
    e = ElementOfPair.of('VREFM')
    assert(e.polarity == PolarityOfPairElement.MINUS)
    assert(e.rank == 1)
    assert(e.prefix == 'VREF')
    e = ElementOfPair.of('whatever')
    assert(e == None)

def test_ElementOfBus():
    e = ElementOfBus.of('CLK0.5')
    assert(e.rank == 0.5)
    assert(e.prefix == 'CLK')
    e = ElementOfBus.of('D15')
    assert(e.rank == 15.0)
    assert(e.prefix == 'D')
    e = ElementOfBus.of('whatever')
    assert(e == None)
