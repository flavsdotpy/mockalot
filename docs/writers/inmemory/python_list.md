---
title: PythonListWriter
parent: InMemory
grand_parent: Writers
---

# PythonListWriter

**`from mockalot.writers import PythonListWriter`**

This writer materialize data as a list of dictionaries into the memory that is returned by the `run` mockalot function.

## Parameters

No parameters available.

## Usage

```python
mockalot.set_writer(PythonListWriter, {})
data = mockalot.run()
print(data[:5])

>
[
    {'name': 'Judith', 'age': 60},
    {'name': 'Terrance', 'age': 62},
    {'name': 'Laurie', 'age': 50},
    {'name': 'Corey', 'age': 55},
    {'name': 'Christopher', 'age': 60} 
]
```
