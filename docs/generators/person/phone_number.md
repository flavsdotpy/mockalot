---
title: PhoneNumberGenerator
parent: Person
grand_parent: Generators
---

# PhoneNumberGenerator

**`from mockalot.generators import PhoneNumberGenerator`**

This generator returns a fake phone number.

## Sample

```python
'364-610-5607'
'(200)462-3029'
'(979)385-3353'
'699-260-9987'
'862-739-2422'
```

## Parameters

No parameters available.

## Validations

There are no validations.

## Usage

```python
mockalot.set_column("my_phone_number", PhoneNumberGenerator, {})
```
