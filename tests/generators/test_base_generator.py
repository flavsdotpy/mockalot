import pytest

from sampy.exceptions import FunctionNotImplementedException
from sampy.generators import Generator


def test_raise_exception_base_generator_instantiated():
    with pytest.raises(TypeError):
        Generator()


def test_raise_exception_method_not_implemented():
    class _FakeGenerator(Generator):
        pass

    with pytest.raises(FunctionNotImplementedException):
        generator = _FakeGenerator()
        generator.generate()
