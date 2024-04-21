---
title: PysparkDataframeWriter
parent: InMemory
grand_parent: Writers
---

# PysparkDataframeWriter

**`from mockalot.writers import PysparkDataframeWriter`**

This writer materialize data as a [Pyspark dataframe](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.html) into the memory that is returned by the `run` mockalot function.

## Parameters

No parameters available.

## Requirements

This writer requires that `pyspark` library is previously installed.  \
Mockalot has facilitated this by addding it as an extra, it's easily installed with `pip install mockalot[pyspark]`.

## Usage

```python
mockalot.set_writer(ParquetWriter, {})
data = mockalot.run()
data.limit(5).show()

>
+---+--------+
|age|    name|
+---+--------+
| 25|   Jason|
| 42| Chelsea|
| 67|  Thomas|
| 41|Victoria|
| 46|    Gina|
+---+--------+
```
