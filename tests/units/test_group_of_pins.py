from electronic_package_descriptor import *
import pytest

def test_that_GroupOfPins_recognizes_ampop_io():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','D+','I','Non inverting input'),
        PinDescription('2','OUT','O','output'),
        PinDescription('3','D-','I','Inverting input')
    ])
    assert(g.pattern == PatternOfGroup.AMPOP_IO)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 3)

def test_that_GroupOfPins_recognizes_ampop_vref():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','VREF+','PWR','Positive voltage reference'),
        PinDescription('2','VREF-','PWR','Negative voltage reference')
    ])
    assert(g.pattern == PatternOfGroup.AMPOP_VREF)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 2)

def test_that_GroupOfPins_recognizes_power():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','VCC','PWR','Power supply'),
        PinDescription('2','VCC','PWR','Power supply'),
        PinDescription('3','VCCA','PWR','Power input for analog part'),
        PinDescription('4','GNDA','GND','Ground for analog part'),
        PinDescription('5','GND','GND','Ground')
    ])
    assert(g.pattern == PatternOfGroup.POWER)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 5)

def test_that_GroupOfPins_recognizes_bus():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','D0','I','Data bus'),
        PinDescription('2','D1','I','Data bus'),
        PinDescription('3','D2','I','Data bus'),
        PinDescription('4','D3','I','Data bus'),
        PinDescription('5','D4','I','Data bus')
    ])
    assert(g.pattern == PatternOfGroup.BUS)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 5)

def test_that_GroupOfPins_recognizes_nothing():
    g = GroupOfPins('gut', 10, 'Group Under Test',[
        PinDescription('1','AS','O','Data bus'),
        PinDescription('2','DS','O','Data bus'),
        PinDescription('3','DTACK','I','Data bus'),
        PinDescription('4','R/W','B','Data bus')
    ])
    assert(g.pattern == None)
    assert(g.designator == 'gut')
    assert(g.rank == 10)
    assert(g.comment == 'Group Under Test')
    assert(len(g.pins) == 4)
