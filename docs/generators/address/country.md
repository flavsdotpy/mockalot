---
title: CountryGenerator
parent: Address
grand_parent: Generators
---

# CountryGenerator

**`from mockalot.generators import CountryGenerator`**

This generator returns a random country name.

## Sample

```python
'Iran'
'Kenya'
'Myanmar'
'Montserrat'
'Ethiopia'
```

## Parameters

No parameters available.

## Validations

There are no validations.

## Usage

```python
mockalot.set_column("my_country", CountryGenerator, {})
```
