import pytest

from mockalot.exceptions import FunctionNotImplementedException
from mockalot.writers import Writer, FileWriter, InMemoryWriter


def test_raise_exception_base_writer_instantiated():
    with pytest.raises(TypeError):
        Writer()


def test_raise_exception_file_writer_instantiated():
    with pytest.raises(TypeError):
        FileWriter()


def test_raise_exception_in_memory_writer_instantiated():
    with pytest.raises(TypeError):
        InMemoryWriter()


def test_raise_exception_base_write_method_not_implemented():
    class _FakeWriter(Writer):
        pass

    with pytest.raises(FunctionNotImplementedException):
        generator = _FakeWriter()
        generator.write(None)


def test_raise_exception_file_write_method_not_implemented():
    class _FakeWriter(FileWriter):
        pass

    with pytest.raises(FunctionNotImplementedException):
        generator = _FakeWriter()
        generator.write(None)


def test_raise_exception_in_memory_write_method_not_implemented():
    class _FakeWriter(InMemoryWriter):
        pass

    with pytest.raises(FunctionNotImplementedException):
        generator = _FakeWriter()
        generator.write(None)
