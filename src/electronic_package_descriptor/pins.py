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
import re

class TypeOfPin(Enum):
    """
    Enumerate the type of pins that can be found in a datasheet.
    """
    POWER = 'PWR'
    GROUND = 'GND'
    DO_NOT_CONNECT = 'DNC'
    INPUT = 'I'
    INPUT_CLOCK = 'ICLK'
    OUTPUT = 'O'
    OUTPUT_CLOCK = 'OCLK'
    OUTPUT_TRISTATE = 'O3'
    OUTPUT_OPEN_COLLECTOR = 'OCOL'
    OUTPUT_OPEN_EMITTER = 'OEMT'
    OUTPUT_PASSIVE = 'OPSV'
    OUTPUT_POWER = 'OPWR'
    BIDIRECTIONNAL_TRISTATE = 'B3'
    BIDIRECTIONNAL = 'B'

class TypeOfPinDesignator(Enum):
    """
    Enumerate the type of designator for a pin, a single number of dip/lcc/sop etc... ; a letter + number for PGA/BGA/...
    """
    NUMBER = 0 # e.g. '1', '2',...
    LETTER_NUMBER = 1 # e.g. 'A1', 'A2',... the letter is the row, the number is the column

class DirectionnalityOfPin(Enum):
    """
    A connected pin is either Input, Output, or Bidirectionnal.

    As a side feature, one can add the int value to the rank to sort the pins grouped by directionnality.
    """
    IN = 0
    OUT = 1000
    BI = 2000

class PolarityOfPairElement(Enum):
    """
    A differential has one 'plus' element and one 'minus' element.

    As a side feature, the order of the enumeration is the order of the elements of a given pair.
    """
    PLUS = 0
    MINUS = 1

class PinDesignator:
    """
    Description of the designator, like '1' or 'M2', into various metrics and predicates.
    """
    def __init__(self, designator: str):
        m = re.match('([A-Z])?([1-9][0-9]*)', designator.upper())
        if m == None:
            raise SyntaxError(f"Unparsable designator '{designator}'")
        g = m.groups() # =(letter or None, number)
        self.type = TypeOfPinDesignator.LETTER_NUMBER if g[0] != None else TypeOfPinDesignator.NUMBER
        if self.type == TypeOfPinDesignator.LETTER_NUMBER:
            self.name_letter = g[0]
            self.name_number = int(g[1])
            self.row = ord(self.name_letter) - ord('A') + 1 # first item is 1
            self.column = self.name_number # first item is 1
            self.rank = (self.row - 1) * 26 + self.name_number
        else:
            self.name_letter = ''
            self.name_number = int(designator)
            self.row = self.name_number # first item is 1
            self.column = self.name_number # first item is 1
            self.rank = self.name_number

class PinDimensions:
    """
    A pin will be stacked, it has a fixed slice thickness of 1 ; the length of the pin name is its spanning.
    """
    def __init__(self, name: str):
        self.thickness = 1
        self.spanning = len(name)

class PinDescription:
    def __init__(self, designator:str, name:str, type:str, description:str):
        self.type = TypeOfPin(type)
        self.designator = PinDesignator(designator)
        self.name = name 
        self.bus = None # TODO detect probable bus.
        self.pair = None # TODO detect probable differential pair
        self.description = description
        self.dimensions = PinDimensions(name)

# debug program
if __name__ == '__main__':
    print('======[ debugPinDesignator ]=======')
    def debugPinDesignator(designator:str):
        try:
            print(f"PinDesignator('{designator}')")
            print(f"    ==> {vars(PinDesignator(designator))}")
        except SyntaxError as err:
            print(f"    ==> {type(err).__name__} : {err}")
    debugPinDesignator('nevermind')
    debugPinDesignator('C12')
    debugPinDesignator('48')

    print('=======[ debugPinDimensions ]=======')
    def debugPinDimensions(name:str):
        print(f"PinDimensions({name})")
        print(f"    ==> {vars(PinDimensions(name))}")
    debugPinDimensions('DTACK')
    debugPinDimensions('VCC')

    print('=======[ debugPinDescription ]=======')
    def debugPinDescription(designator:str, name:str, type:str, description:str):
        try:
            print(f"debugPinDescription({designator},{name},{type},{description})")
            pds = PinDescription(designator, name, type, description)
            print(f"    ==> {vars(pds)}")
            print(f"    ==> {vars(pds.designator)}")
            print(f"    ==> {vars(pds.dimensions)}")
        except ValueError as err:
            print(f"    ==> {err}")
    debugPinDescription('32','DTACK','O','DaTa ACKnowledge')
    debugPinDescription('D10','DTACK','WTV','DaTa ACKnowledge')
