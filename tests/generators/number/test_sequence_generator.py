from mockalot.generators import SequenceGenerator


def test_generate_sequence():
    generator = SequenceGenerator()
    seq_list = [generator.generate() for _ in range(5)]
    assert seq_list == [1,2,3,4,5]


def test_generate_sequence_start_set():
    generator = SequenceGenerator(start=101)
    seq_list = [generator.generate() for _ in range(5)]
    assert seq_list == [101,102,103,104,105]


def test_generate_sequence_jump_set():
    generator = SequenceGenerator(jump=2)
    seq_list = [generator.generate() for _ in range(5)]
    assert seq_list == [1,3,5,7,9]
