---
title: PandasDataframeWriter
parent: InMemory
grand_parent: Writers
---

# PandasDataframeWriter

**`from mockalot.writers import PandasDataframeWriter`**

This writer materialize data as a [Pandas dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) into the memory that is returned by the `run` mockalot function.

## Parameters

No parameters available.

## Requirements

This writer requires that `pyspark` library is previously installed.  \
Mockalot has facilitated this by addding it as an extra, it's easily installed with `pip install mockalot[pyspark]`.

## Usage

```python
mockalot.set_writer(PandasDataframeWriter, {})
data = mockalot.run()
print(data.head(5))

>
          name  age
0  Christopher   36
1       Robert   56
2        Aaron   66
3      Anthony   40
4       Angela   55
```
