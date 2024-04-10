import pathlib

from ..config import Defaults
from ..exceptions import FunctionNotImplementedException
from ..log import get_logger


class Writer:

    def __init__(self, *_, **__):
        if type(self) == Writer:
            raise TypeError("Cannot instantiate SuperClass directly")

    def write(self, data: list[dict]):
        raise FunctionNotImplementedException("Not yet implemented!")


class FileWriter(Writer):

    _EXTENSION = ""

    def __init__(self, *args, output_filename: str = Defaults.OUTPUT_FILENAME, output_path: str = Defaults.OUTPUT_PATH, **kwargs):
        if type(self) == FileWriter:
            raise TypeError("Cannot instantiate SuperClass directly")
        super().__init__(*args, **kwargs)
        self.output_file = f"{output_path}/{output_filename}.{self._EXTENSION}"

    def _prepare_path(self, ):
        pathlib.Path(self.output_file).parent.mkdir(parents=True, exist_ok=True)
        get_logger().debug(f"Writing to {self.output_file}")


class InMemoryWriter(Writer):

    def __init__(self, *args, **kwargs):
        if type(self) == InMemoryWriter:
            raise TypeError("Cannot instantiate SuperClass directly")
        super().__init__(*args, **kwargs)
