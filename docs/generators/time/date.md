---
title: DateGenerator
parent: Time
grand_parent: Generators
---

# DateGenerator

**`from mockalot.generators import DateGenerator`**

This generator returns a random datetime.date object.

## Sample

```python
'2023-10-01'
'2023-09-23'
'2023-06-30'
'2024-03-22'
'2024-01-17'
```

## Parameters

### min (datetime.date)

The lower boundary for the generated date.  \
It defaults to `current_date - 365 days`.

### max (datetime.date)

The higher boundary for the generated date.  \
It defaults to `current_date`.

## Validations

`min` **MUST** be always lower than `max`.

## Usage

### Simple

```python
mockalot.set_column("my_date", DateGenerator, {})
```

### Complete

```python
params = {
    "min": date(2000,1,1),
    "max": date(2023,12,31),
}
mockalot.set_column("my_date", DateGenerator, params)
```
