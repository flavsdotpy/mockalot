from typing import Any, Type

from sampy.config import Defaults
from sampy.exceptions import InvalidParameterException
from sampy.generators import Generator
from sampy.log import get_logger
from sampy.writers import Writer


class Sampy:

    __DEFAULT_CONFIG = {
        "sample_size": Defaults.SAMPLE_SIZE
    }

    def __init__(self):
        self.__generators = {}
        self.__writer = None
        self.__config = self.__DEFAULT_CONFIG.copy()

    def set_writer(self, writer: Type[Writer], params: dict = None):
        self.__writer = writer(**params)
        return self

    def get_writer(self):
        return self.__writer

    def set_config(self, key: str, value: Any):
        if key not in self.__DEFAULT_CONFIG:
            raise InvalidParameterException(f"Configuration {key} does not exist!")
        self.__config[key] = value
        return self

    def get_config(self, key: str):
        if key not in self.__DEFAULT_CONFIG:
            raise InvalidParameterException(f"Configuration {key} does not exist!")
        return self.__config[key]

    def set_column(self, column_name: str, generator: Generator, parameters: dict):
        self.__generators[column_name] = generator(**parameters)
        return self

    def get_column(self, column_name: str):
        if column_name not in self.__generators:
            raise InvalidParameterException(f"Column {column_name} not set!")
        return self.__generators[column_name]

    def get_columns(self, name_only: bool = False):
        if name_only:
            return list(self.__generators.keys())
        return self.__generators

    def __generate(self):
        get_logger().info("Generating data...")
        get_logger().debug(f"Config -----------")
        get_logger().debug(str(self.__config))
        get_logger().debug("Columns ----------")
        for col, col_conf in self.__generators.items():
            get_logger().debug(f"Column: {col} Generator: {col_conf}")
        self.data = [{
            col: generator.generate()
            for col, generator in self.__generators.items()
        } for _ in range(self.__config["sample_size"])]
        return self.data

    def __write(self):
        get_logger().info("Writing data...")
        get_logger().debug(f"Output file: {self.__writer.output_file}")
        self.__writer.write(self.data)

    def run(self):
        self.__generate()
        self.__write()
