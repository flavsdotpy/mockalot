from typing import Any

from ..exceptions import FunctionNotImplementedException


class Generator:

    def __init__(self):
        if type(self) == Generator:
            raise TypeError("Cannot instantiate SuperClass directly")

    def generate(self) -> Any:
        raise FunctionNotImplementedException("generate() not implemented!")
