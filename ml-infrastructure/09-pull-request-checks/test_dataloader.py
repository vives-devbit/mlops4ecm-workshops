"""Unit tests for data_utils.py"""

from data_utils import add_numbers, is_even


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
