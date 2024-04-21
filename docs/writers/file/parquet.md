---
title: ParquetWriter
parent: File
grand_parent: Writers
---

# ParquetWriter

**`from mockalot.writers import ParquetWriter`**

This writer materialize data as a `.parquet` file into the file system.

## Parameters

### output_path (str)

The target path of the outputed parquet.  \
It defaults to `./output`

### output_filename (str)

The name of the outputed parquet.  \
It defaults to `sample_data`.  \
_Obs: There is no need to include the extesion (`.parquet`) as it's automatically set!_

## Requirements

This writer requires that `pyarrow` library is previously installed.  \
Mockalot has facilitated this by addding it as an extra, it's easily installed with `pip install mockalot[parquet]`.

## Usage

### Simple

```python
mockalot.set_writer(ParquetWriter, {})
```

### Complete

```python
from mockalot.writers import ParquetWriter

writer_params = {
    "output_path": "/path/to/file",
    "output_filename": "my_parquet_file",
}
mockalot.set_writer(ParquetWriter, writer_params)
```
