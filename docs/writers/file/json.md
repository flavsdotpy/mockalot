---
title: JsonWriter
parent: File
grand_parent: Writers
---

# JsonWriter

**`from mockalot.writers import JsonWriter`**

This writer materialize data as a `.json` file into the file system.

## Parameters

### output_path (str)

The target path of the outputed json.  \
It defaults to `./output`

### output_filename (str)

The name of the outputed json.  \
It defaults to `sample_data`.  \
_Obs: There is no need to include the extesion (`.json`) as it's automatically set!_

### jsonlines (boolean)

If true, the outputed json will be a [jsonlines](https://jsonlines.org/) file.

## Usage

### Simple

```python
mockalot.set_writer(JsonWriter, {})
```

### Complete

```python
params = {
    "output_path": "/path/to/file",
    "output_filename": "my_json_file",
    "jsonlines": True
}
mockalot.set_writer(JsonWriter, params)
```
