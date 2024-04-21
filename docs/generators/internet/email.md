---
title: EmailGenerator
parent: Internet
grand_parent: Generators
---

# EmailGenerator

**`from mockalot.generators import EmailGenerator`**

This generator returns a fake email address.

## Sample

```python
'bsmith@sawyer-thomas.biz'
'joseph03@lopez.com'
'thomasshaw@brown-sampson.com'
'michellecarrillo@caldwell.com'
'sarah26@montes-guerrero.org'
```

## Parameters

### safe_domain (bool)

If `True`, return a safe domain, like `example.org`, instead of a fake domain.  \
It defaults to `False`.

### public_domain (bool)

If `True`, return a public domain, like `gmail.com` instead of a fake domain.  \
It defaults to `False`.

### anon_username (bool)

If `True`, return a random string of 12 characters, like `jhdnaosdnsad`, instead of a fake username.  \
It defaults to `False`.

## Validations

`safe_domain` and `public_domain` are mutually exclusive, so they **CANNOT** be true at the same time.

## Usage

### Simple

```python
mockalot.set_column("my_email", EmailGenerator, {})
```

### Complete

```python
params_a = {
    "safe_domain": True,
    "anon_username": True,
}
mockalot.set_column("my_email_a", EmailGenerator, params_a)

params_b = {
    "public_domain": True,
    "anon_username": True,
}
mockalot.set_column("my_email_b", EmailGenerator, params_b)
```
