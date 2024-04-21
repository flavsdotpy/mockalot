---
title: CSVWriter
parent: File
grand_parent: Writers
---

# CSVWriter

**`from mockalot.writers import CSVWriter`**

This writer materialize data as a `.csv` file into the file system.

## Parameters

### output_path (str)

The target path of the outputed csv.  \
It defaults to `./output`

### output_filename (str)

The name of the outputed csv.  \
It defaults to `sample_data`.  \
_Obs: There is no need to include the extesion (`.csv`) as it's automatically set!_

## Usage

### Simple

```python
mockalot.set_writer(CSVWriter, {})
```

### Complete

```python
params = {
    "output_path": "/path/to/file",
    "output_filename": "my_csv_file",
}
mockalot.set_writer(CSVWriter, params)
```
