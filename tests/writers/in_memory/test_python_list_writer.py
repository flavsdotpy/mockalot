from mockalot.writers import PythonListWriter


TEST_DATA = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]


def test_pyspark_writer_write():
    writer = PythonListWriter()
    
    returned_value = writer.write(TEST_DATA)

    assert returned_value == TEST_DATA
