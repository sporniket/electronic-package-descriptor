# Sporniket's electronic package descriptor

> [WARNING] Please read carefully this note before using this project. It contains important facts.

Content

1. What is **Sporniket's electronic package descriptor**, and when to use it ?
2. What should you know before using **Sporniket's electronic package descriptor** ?
3. How to use **Sporniket's electronic package descriptor** ?
4. Known issues
5. Miscellanous

## 1. What is **Sporniket's electronic package descriptor**, and when to use it ?

**Sporniket's electronic package descriptor** is a python library that provide an abstract model and API for helping generate component symbols for EDA suites like Kicad.


### Licence

**Sporniket's electronic package descriptor** is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

**Sporniket's electronic package descriptor** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

### Release notes

#### v0.0.2

* The model of a group of pins is complete

#### v0.0.1

* the model of a pin is complete

## 2. What should you know before using **Sporniket's electronic package descriptor** ?

**Sporniket's electronic package descriptor** is written using python version 3.6, and should work with python version 3.7 up to 3.10.

It relies on the following packages to build and test :
* build
* pytest

see [README packaging](https://github.com/sporniket/electronic-package-descriptor/blob/main/README-packaging.md) for further details.

> Do not use **Sporniket's electronic package descriptor** if this project is not suitable for your project.

## 3. How to use **Sporniket's electronic package descriptor** ?

### From sources

To get the latest available models, one must clone the git repository, build and install the package.

	git clone https://github.com/sporniket/electronic-package-descriptor.git
	cd electronic-package-descriptor
	python3 -m build && python3 -m pip install --force-reinstall dist/*.whl

Then, import the library in your code :

```python
from electronic_package_descriptor import *
```

### Using pip

```
pip install electronic-package-descriptor-by-sporniket
```

Then, import the library in your code :

```python
from electronic_package_descriptor import *
```

## 4. Known issues
See the [project issues](https://github.com/sporniket/electronic-package-descriptor/issues) page.

## 5. Miscellanous

### Report issues
Use the [project issues](https://github.com/sporniket/electronic-package-descriptor/issues) page.
