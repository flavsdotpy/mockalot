from datetime import date

from sampy import Sampy
from sampy.generators import FloatGenerator, EmailGenerator, DateGenerator, UUIDGenerator, \
                             NameGenerator, PickFromListGenerator, CityGenerator, CountryGenerator, \
                             PhoneNumberGenerator
from sampy.log import get_logger
from sampy.writers import JsonWriter, CSVWriter


def main():
    get_logger().info("Started processing...")

    get_logger().info("Building customers...")
    customers_generator = Sampy() \
        .set_writer(JsonWriter, {"output_filename": "customers"}) \
        .set_config("sample_size", 2000) \
        .set_column("id", UUIDGenerator, {}) \
        .set_column("name", NameGenerator, {}) \
        .set_column("email", EmailGenerator, {})
    customers_generator.run()
    customers_ids = [c["id"] for c in customers_generator.data]

    get_logger().info("Building stores...")
    stores_generator = Sampy() \
        .set_writer(JsonWriter, {"output_filename": "stores"}) \
        .set_config("sample_size", 200) \
        .set_column("id", UUIDGenerator, {}) \
        .set_column("city", CityGenerator, {}) \
        .set_column("country", CountryGenerator, {}) \
        .set_column("contact", PhoneNumberGenerator, {}) \
        .set_column("manager", NameGenerator, {})
    stores_generator.run()
    stores_ids = [c["id"] for c in stores_generator.data]

    get_logger().info("Building orders...")
    orders_generator = Sampy() \
        .set_writer(CSVWriter, {"output_filename": "orders"}) \
        .set_config("sample_size", 100000) \
        .set_column("order_id", UUIDGenerator, {}) \
        .set_column("customer_id", PickFromListGenerator, {"elements": customers_ids}) \
        .set_column("store_id", PickFromListGenerator, {"elements": stores_ids}) \
        .set_column("value", FloatGenerator, {"start": 1000, "end": 10000}) \
        .set_column("date", DateGenerator, {"start": date(2023,1,1), "end": date(2023,12,31)})
    orders_generator.run()

    get_logger().info("Finished processing...")


if __name__ == "__main__":
    main()
