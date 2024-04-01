import csv
import json
import pathlib

from sampy.config import Defaults
from sampy.exceptions import FunctionNotImplementedException
from sampy.log import get_logger


class Writer:

    _EXTENSION = ""

    def __init__(self, output_filename: str = Defaults.OUTPUT_FILENAME, output_path: str = Defaults.OUTPUT_PATH):
        if type(self) == Writer:
            raise TypeError("Cannot instantiate SuperClass directly")
        self.output_file = f"{output_path}/{output_filename}.{self._EXTENSION}"

    def _prepare_path(self, ):
        pathlib.Path(self.output_file).parent.mkdir(parents=True, exist_ok=True)

    def write(self, data: list[dict]):
        raise FunctionNotImplementedException("Not yet implemented!")



class CSVWriter(Writer):

    _EXTENSION = "csv"

    def write(self, data: list[dict]):
        self._prepare_path()
        with open(self.output_file, "w") as fout:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


class JsonWriter(Writer):

    _EXTENSION = "json"

    def __init__(self, jsonlines: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.jsonlines = jsonlines

    def __write_json_doc(self, data: list[dict]):
        with open(self.output_file, "w") as fout:
            fout.write(json.dumps(data))

    def __write_jsonlines(self, data: list[dict]):
        with open(self.output_file, "w") as fout:
            for row in data:
                fout.write(json.dumps(row))
                fout.write("\n")

    def write(self, data: list[dict]):
        self._prepare_path()
        if self.jsonlines:
            self.__write_jsonlines(data)
        else:
            self.__write_json_doc(data)

