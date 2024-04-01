# mockalot

[![codecov](https://codecov.io/gh/flavsdotpy/mockalot/master/graph/badge.svg?token=FMD26G97A7)](https://codecov.io/gh/flavsdotpy/mockalot)
![example workflow](https://github.com/flavsdotpy/mockalot/actions/workflows/ci.yml/badge.svg)

> :warning: **Work In Progress**: Library still in very early stages!

Sample data generator library.  \
The motivation to create this project was the high number of limitations for similar web apps in the free tier. This is easy to run locally, at Jupyter or even have it as a library for other projects.

# Features

This is a library to help with sample data generation in a number of different ways:
> - Modular generators to help you get single random values
> - Full-scope class to generate batches of data
> - Modular writers to have your sample data writen directly into the most popular formats.

# Usage

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

# Roadmap

You can see the project's roadmap [here](https://github.com/flavsdotpy/mockalot/issues).

# Author

* **[flavsdotpy](https://github.com/flavsdotpy)**

# License

mockalot is available under the MIT license. See the LICENSE file for more info.
