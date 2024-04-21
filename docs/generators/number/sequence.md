---
title: SequenceGenerator
parent: Number
grand_parent: Generators
---

# SequenceGenerator

**`from mockalot.generators import SequenceGenerator`**

This generator returns sequenced data.

## Sample

```python
1
2
3
4
5
```

## Parameters

### start (int)

The start of the sequence.  \
It defaults to `1`.

### jump (int)

The increments of the sequence.  \
It defaults to `1`.

## Validations

There are no validations.

## Usage

### Simple

```python
mockalot.set_column("my_seq", SequenceGenerator, {})
```

### Complete

```python
params = {
    "start": 1000,
    "jump": 10,
}
mockalot.set_column("my_seq", SequenceGenerator, {})
```
