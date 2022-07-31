# Specifications for the Json descriptor of an IC

> inspired by https://github.com/sporniket/kicad-scripts/blob/legacy/symbol-generator--ic/jsonFromDatasheet.py

## Root

```jsonc
{
  "meta": {
    //meta data
  },
  "pins": [
    //an array of pin descriptions.
  ],
  "groups": {
    //an array of group descriptions.
  }
}
```

### meta

```jsonc
{
  "name": "MC68000_PLCC_68", //symbol name
  "aliases": [ "MC68010", "MC68HC000" ], //Array of alternative names
  "reference": "U", //reference prefix
  "datasheet": "https://...", // Url of the datasheet
  "footprint": "Package_LCC:PLCC-68_THT-Socket", //Name of a builtin footprint
  "physical": "LCC" //model of the physical layout of the pins
}
```

> **Values for `physical`**
> 
> * BRD (board) : pins are on the left and the right of the symbol, the first half on the left, the second half on the right, each side starting from the top to the bottom.
> * DIM : DIM (Dual Inline Module), left side are odd pins, right side are even pins. Applicable to DIMM (Dual Inline Memory Module), and could also work for pcb edge connectors.
> * DIP : pins are on the left and the right of the symbol, laid out counter-clock-wise starting with the first pin at the top left position.
> * LCC : pins are on the four sides of the symbol, laid out counter-clock-wise starting with the first pin at the middle of the top side. (Some manufacturers may deviate from this convention)
> * QFP : pins are on the four sides of the symbol, laid out counter-clock-wise starting with the first pin at the top of the left side. (Some manufacturers may deviate from this convention)
> * SIM : SIM (Single Inline Module), pins are all on the left. Applicable to SIMM (Single Inline Memory Module).

### pins

> an array of pin descriptions.

```jsonc
{
  "designator": "1", //either a number, or a letter + number
  "name": "D4", //pin name
  "type": "B", //String encoding the type of pin
  "group": "DATA", // designator of the group
  "description": "Data value" // human readable description
}
```

### groups

> an array of group descriptions

```jsonc
{
  "designator": "DATA", //a unique codename
  "rank": 1010, //rank for sorting
  "comment": "CPU bus data", //Used as the sub-unit subtitle
  "pins" : ["1","2","3"] //An array of pin designators of the pins that makes the group.
}
```
