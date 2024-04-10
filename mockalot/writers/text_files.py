import csv
import json

from ._base import FileWriter


class CSVWriter(FileWriter):

    _EXTENSION = "csv"

    def write(self, data: list[dict]):
        self._prepare_path()
        with open(self.output_file, "w") as fout:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


class JsonWriter(FileWriter):

    _EXTENSION = "json"

    def __init__(self, jsonlines: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
