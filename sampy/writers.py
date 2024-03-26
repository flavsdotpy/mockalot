import csv
import json
import pathlib

from sampy.config import Defaults
from sampy.log import get_logger


class BaseWriter:

    _EXTENSION = ""

    def __init__(self, output_filename: str = Defaults.OUTPUT_FILENAME, output_path: str = Defaults.OUTPUT_PATH):
        self.output_file = f"{output_path}/{output_filename}.{self._EXTENSION}"

    def _prepare_path(self, ):
        pathlib.Path(self.output_file).parent.mkdir(parents=True, exist_ok=True)

    def write(self, data: list[dict]):
        raise Exception("Not yet implemented!")



class CSVWriter(BaseWriter):

    _EXTENSION = "csv"

    def write(self, data: list[dict]):
        self._prepare_path()
        with open(self.output_file, "w") as fout:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


class JsonWriter(BaseWriter):

    _EXTENSION = "json"

    def __init__(self, jsonlines: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.jsonlines = jsonlines

    def write(self, data: list[dict]):
        self._prepare_path()
        with open(self.output_file, "w") as fout:
            if self.jsonlines:
                for row in data:
                    fout.write(json.dumps(row))
                    fout.write("\n")
            else:
                fout.write(json.dumps(data))


def get_writer_by_output_format(output_format):
    writer = {
        "csv": CSVWriter,
        "json": JsonWriter
    }.get(output_format)
    if not writer:
        raise Exception(f"Writer not found for format: {output_format}")
    get_logger().info(f"Writer: {writer.__name__}")
    return writer
