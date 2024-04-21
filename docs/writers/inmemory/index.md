---
title: InMemory
parent: Writers
has_children: True
---

# InMemory

Writer classes that materialize generated data as logical structures into the memory.

## Usage

When set as the writer for mockalot, you can retrieve the return value from the `run` function as a variable and work with it. Ex.:

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
