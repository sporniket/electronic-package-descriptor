> This document specifies the structure that a datasheet MUST follow in order to be parsed.
>
> Blockquotes serve as comment blocks, and are ignored

# Name_of_the_Integrated_Circuit

> The title is the name of the electronic package.


## Symbol

> Optional section.
>
> This section MAY contains a bullet list to define some metadatas of the electronic package.
>
> When a metadata is missing, it will either take a default value (reference, pins layout) or stay undefined/empty (aliases, datasheet and footprint).

* Aliases : AKA1, AKA2
* Reference : U
* Datasheet : http://...
* Footprint : package_name:footprint_id
* Pins layout : DIP

> pins layout : DIP (default), BRD, LCC, QFP

## Pinout

> Mandatory section.
>
> A table describing all the pins of the electronic package, with the following columns :
>
> * **Pin** : the index of the pin
> * **Name** : the name or the list of names separated by space of the signal. Names of active low signals are prefixed with `/`. E.g. single name 'OE', low active single name '/DTACK', multiple name 'R /W' (High 'Read', Low 'Write', note the space between 'R' and '/W').
> * **Pin Type** : a case insensitive code, see the list below.
> * **Group** : fonctionnal group of the pin. The pins of a bus SHOULD constitute a group. Pins of type *PWR*, *GND* and *DNC* SHOULD be in an empty group.
> * **Comment** : supplemental description of the pin.
>
>
> The pin type is a value among the following list designed to accomodate kicad classification/specialization :
>
> * **PWR** : Power Voltage entry
> * **GND** : Power ground
> * **DNC** : «Do Not Connect»
> * **I** : Generic Input
> * **ICLK** : Input of a clock signal
> * **O** : Generic Output
> * **OCLK** : Output of a clock signal
> * **O3** : Three-state output
> * **OCOL** : Open collector output
> * **OEMT** : Open emitter output
> * **OPWR** : Power output
> * **B** : Bidirectionnal


|Pin|Name|Pin Type|Group|Comment|
|---|---|---|---|---|

### Pin groups

> Mandatory section.
>
> A table describing each group, with the following columns :
>
> * **Group id** : the id of the group (e.g. 'ADDR', 'DATA',...)
> * **Rank** : specify an index to rank the group
> * **Comment** : human readable description.
>
>


|Group id|Rank|Comment|
|---|---|---|

> From this point onward, the remaining of the document is ignored

## Whatever

> Complement the datasheet to your liking.
