from typing import Any, Type

from sampy.config import Defaults
from sampy.generators import BaseGenerator
from sampy.log import get_logger
from sampy.writers import BaseWriter


class Sampy:

    __DEFAULT_CONFIG = {
        "sample_size": Defaults.SAMPLE_SIZE
    }

    def __init__(self):
        self.generators = {}
        self.writer = None
        self.config = self.__DEFAULT_CONFIG.copy()

    def set_writer(self, writer: Type[BaseWriter], params: dict = None):
        self.writer = writer(**params)
        return self

    def set_config(self, key: str, value: Any):
        self.config[key] = value
        return self

    def set_configs(self, **configs):
        self.config.update(configs)
        return self

    def add_column(self, column_name: str, generator: BaseGenerator, parameters: dict):
        if column_name in self.generators:
            raise Exception(f"Column {column_name} already exists!")
        self.generators[column_name] = {
            "class": generator,
            "params": parameters
        }
        return self

    def add_columns(self, *columns):
        self.generators.update({
            col["name"]: {
                "class": col["generator"],
                "params": col["parameters"]
            }
            for col in columns
        })
        return self

    def validate(self):
        if self.config["sample_size"] <= 0:
            raise Exception("Sample size can't be lower or equal than 0")

    def generate(self):
        get_logger().info("Generating data...")
        get_logger().info(f"Config -----------")
        get_logger().info(str(self.config))
        get_logger().info("Columns ----------")
        for col, col_conf in self.generators.items():
            get_logger().info(f"Column: {col} Generator: {col_conf['class'].__name__}")
        self.data = [{
            col: col_conf["class"].generate(**col_conf["params"])
            for col, col_conf in self.generators.items()
        } for _ in range(self.config["sample_size"])]
        return self.data

    def write(self):
        get_logger().info("Writing data...")
        get_logger().info(f"Output file: {self.writer.output_file}")
        self.writer.write(self.data)
