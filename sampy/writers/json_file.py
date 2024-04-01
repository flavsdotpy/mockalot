import json

from ._base import Writer


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
