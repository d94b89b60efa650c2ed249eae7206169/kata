# content of test_sample.py
from src.sample import func


def test_answer():
    assert func(4) == 5
