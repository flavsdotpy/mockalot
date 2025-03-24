# mockalot

[![codecov](https://codecov.io/gh/flavsdotpy/mockalot/master/graph/badge.svg?token=FMD26G97A7)](https://codecov.io/gh/flavsdotpy/mockalot)&nbsp;&nbsp;
![example workflow](https://github.com/flavsdotpy/mockalot/actions/workflows/ci.yml/badge.svg)

Sample data generator library.  \
This is easy to run locally, in a Jupyter notebook or even have it as a library for other projects.

## Features

* Generates sample data in the form of physical files, in the most popular formats, like `csv` and `parquet`.
* Generates sample data in the form of in-memory structures, like list of dictionaries or even table objects like Pandas or Pyspark dataframes.
* Highly customizable column types.
* Modular structure, you can even create your own classes if you want.

## How to install it?

Run `pip install mockalot`

### Extras

To make use of parquet, pandas or pyspark, extra packges were included. You can run `pip install mockalot[parquet]` and easily install all the necessary libraries to work with parquet. This is not mandatory tho, so if you are in an environment that has everything installed out-of-the box (AWS Glue, Databricks, etc), you can use Mockalot without worrying with extras.

## Usage

```python
from mockalot import Mockalot
from mockalot.generators import EmailGenerator, UUIDGenerator, NameGenerator
from mockalot.writers import CSVWriter

mocker = Mockalot()

mocker.set_config("sample_size", 20000) \
      .set_column("id", UUIDGenerator, {}) \
      .set_column("name", NameGenerator, {}) \
      .set_column("email", EmailGenerator, {}) \
      .set_writer(CSVWriter, {"output_filename": "users"})

mocker.run()
```

The snipped above will create a CSV file of 20k lines, consisted of 3 columns(id, name and email), written into `./output/users.csv`.

There are more usage examples [here](./examples/).

## Roadmap

You can see the project's roadmap [here](https://github.com/flavsdotpy/mockalot/issues).

## Considerations

The motivation to create this project was the high number of limitations for similar web apps in the free tier. 

## Author

* **[flavsdotpy](https://github.com/flavsdotpy)**

## License

mockalot is available under the MIT license. See the LICENSE file for more info.
