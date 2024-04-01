import pathlib

from ..config import Defaults
from ..exceptions import FunctionNotImplementedException


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
