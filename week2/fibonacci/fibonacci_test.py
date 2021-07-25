import pytest
from fibonacci import find_nth_fibonacci

def test_negative_n():
    assert find_nth_fibonacci(-1) == None

def test_zero():
    assert find_nth_fibonacci(0) == None

def test_n_not_integer():
    assert find_nth_fibonacci(2.5) == None

def test_first_fibonnaci():
    assert find_nth_fibonacci(1) == 0

def test_second_fibonnaci():
    assert find_nth_fibonacci(2) == 1

def test_valid_n():
    assert find_nth_fibonacci(6) == 5