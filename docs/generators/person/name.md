---
title: NameGenerator
parent: Person
grand_parent: Generators
---

# NameGenerator

**`from mockalot.generators import NameGenerator`**

This generator returns a fake name. 

## Sample

```python
'Nancy Reid'
'Valerie Walker'
'Matthew Smith'
'Christopher Huber'
'Phillip Mclean'
```

## Parameters

### last_name_only (bool)

If `True`, return only the last name.  \
It defaults to `False`.

### first_name_only (bool)

If `True`, return only the first name.  \
It defaults to `False`.

## Validations

`last_name_only` and `first_name_only` are mutually exclusive, so they **CANNOT** be true at the same time.

## Usage

### Simple

```python
mockalot.set_column("my_name", NameGenerator, {})
```

### Complete

```python
params_last_name = {
    "last_name_only": True,
}
mockalot.set_column("my_last_name", NameGenerator, params_last_name)

params_first_name = {
    "first_name_only": True,
}
mockalot.set_column("my_first_name", NameGenerator, params_first_name)
```
