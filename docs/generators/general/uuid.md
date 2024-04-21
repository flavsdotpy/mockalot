---
title: UUIDGenerator
parent: General
grand_parent: Generators
---

# UUIDGenerator

**`from mockalot.generators import UUIDGenerator`**

This generator returns a random UUID.

## Sample

```python
'dab46b1d-19d1-4c9c-9025-519372cdadb5'
'1cc301c8-8c46-4278-9e2f-58cfe3e2d2e9'
'5eca3887-2e4c-4126-9cff-e05a503c255a'
'9d842d92-68a9-4f10-a71e-d45fa905fdcc'
'c20b9241-1231-4d83-952e-c51358e8b649'
```

## Parameters

No parameters available.

## Validations

There are no validations.

## Usage

```python
mockalot.set_column("my_uuid", UUIDGenerator, {})
```
