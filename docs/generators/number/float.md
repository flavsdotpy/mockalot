---
title: FloatGenerator
parent: Number
grand_parent: Generators
---

# FloatGenerator

**`from mockalot.generators import FloatGenerator`**

This generator returns a random float.

## Sample

```python
570.2
299.41
775.99
164.15
548.29
```

## Parameters

### min (float)

The lower boundary for the generated float.  \
It defaults to `1.0`.

### max (float)

The higher boundary for the generated float.  \
It defaults to `1000.0`.

### decimal_places (int)

The number of decimal places for the generated float.  \
It default to `2`.

## Validations

* `min` **MUST** be always lower than `max`.
* The difference between `min` and `max` must be greater than `0.1`

## Usage

### Simple

```python
mockalot.set_column("my_float", FloatGenerator, {})
```

### Complete

```python
params = {
    "min": 0.0,
    "max": 10.0,
    "decimal_places": 4
}
mockalot.set_column("my_float", FloatGenerator, params)
```
