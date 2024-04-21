---
title: CityGenerator
parent: Address
grand_parent: Generators
---

# CityGenerator

**`from mockalot.generators import CityGenerator`**

This generator returns a random city name.

## Sample

```python
'South Jonathon'
'Williamsside'
'New Johnnyhaven'
'South Brittany'
'Kennethville'
```

## Parameters

No parameters available.

## Validations

There are no validations.

## Usage

```python
mockalot.set_column("my_city", CityGenerator, {})
```
