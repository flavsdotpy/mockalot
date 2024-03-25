from datetime import date

from sampy import Sampy
from sampy.config import Defaults
from sampy.generators import FloatGenerator, EmailGenerator, DateGenerator, UUIDGenerator, \
                             NameGenerator, PickFromListGenerator, CityGenerator, CountryGenerator, \
                             PhoneNumberGenerator
from sampy.log import get_logger
from sampy.writers import JsonWriter, CSVWriter


def main():
    get_logger().info("Started processing...")

    get_logger().info("Building customers...")
    customers_generator = Sampy() \
        .set_writer(JsonWriter, {"output_path": Defaults.OUTPUT_PATH, "output_filename": "customers"}) \
        .set_config("sample_size", 2000) \
        .add_column("id", UUIDGenerator, {}) \
        .add_column("name", NameGenerator, {}) \
        .add_column("email", EmailGenerator, {})
    customers_generator.validate()
    customers_generator.generate()
    customers_generator.write()
    customers_ids = [c["id"] for c in customers_generator.data]

    get_logger().info("Building stores...")
    stores_generator = Sampy() \
        .set_writer(JsonWriter, {"output_path": Defaults.OUTPUT_PATH, "output_filename": "stores"}) \
        .set_config("sample_size", 200) \
        .add_column("id", UUIDGenerator, {}) \
        .add_column("city", CityGenerator, {}) \
        .add_column("country", CountryGenerator, {}) \
        .add_column("contact", PhoneNumberGenerator, {}) \
        .add_column("manager", NameGenerator, {})
    stores_generator.validate()
    stores_generator.generate()
    stores_generator.write()
    stores_ids = [c["id"] for c in stores_generator.data]

    get_logger().info("Building orders...")
    orders_generator = Sampy() \
        .set_writer(CSVWriter, {"output_path": Defaults.OUTPUT_PATH, "output_filename": "orders"}) \
        .set_config("sample_size", 100000) \
        .add_column("order_id", UUIDGenerator, {}) \
        .add_column("customer_id", PickFromListGenerator, {"elements": customers_ids}) \
        .add_column("store_id", PickFromListGenerator, {"elements": stores_ids}) \
        .add_column("value", FloatGenerator, {"start": 1000, "end": 10000}) \
        .add_column("date", DateGenerator, {"start": date(2023,1,1), "end": date(2023,12,31)})
    orders_generator.validate()
    orders_generator.generate()
    orders_generator.write()

    get_logger().info("Finished processing...")


if __name__ == "__main__":
    main()
