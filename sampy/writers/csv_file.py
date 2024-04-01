import csv

from ._base import Writer

class CSVWriter(Writer):

    _EXTENSION = "csv"

    def write(self, data: list[dict]):
        self._prepare_path()
        with open(self.output_file, "w") as fout:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(fout, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
