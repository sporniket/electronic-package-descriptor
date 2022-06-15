from electronic_package_descriptor.pins import *
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
