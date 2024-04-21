---
title: PickFromListGenerator
parent: General
grand_parent: Generators
---

# PickFromListGenerator

**`from mockalot.generators import PickFromListGenerator`**

This generator returns a random element of a given list.

## Sample (_elements begin ascii letters_)

```python
'K'
'f'
'e'
'O'
'y'
```

## Parameters

### elements (list)

List of elements to be picked from.

## Validations

`elements` **MUST** be a list of at least two elements.

## Usage

```python
elements = ["a", "b", "c"]
mockalot.set_column("my_element", PickFromListGenerator, {"elements": elements})
```
