---
title: IntegerGenerator
parent: Number
grand_parent: Generators
---

# IntegerGenerator

**`from mockalot.generators import IntegerGenerator`**

This generator returns a random integer.

## Sample

```python
432
91
176
75
5
```

## Parameters

### min (int)

The lower boundary for the generated integer.  \
It defaults to `1`.

### max (int)

The higher boundary for the generated integer.  \
It defaults to `1000`.

## Validations

`min` **MUST** be always lower than `max`.

## Usage

### Simple

```python
mockalot.set_column("my_integer", IntegerGenerator, {})
```

### Complete

```python
params = {
    "min": 1000,
    "max": 100000,
}
mockalot.set_column("my_integer", IntegerGenerator, params)
```
