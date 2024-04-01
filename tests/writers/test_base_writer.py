import pytest

from mockalot.exceptions import FunctionNotImplementedException
from mockalot.writers import Writer


def test_raise_exception_base_generator_instantiated():
    with pytest.raises(TypeError):
        Writer()


def test_raise_exception_method_not_implemented():
    class _FakeWriter(Writer):
        pass

    with pytest.raises(FunctionNotImplementedException):
        generator = _FakeWriter()
        generator.write(None)
