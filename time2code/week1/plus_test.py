import pytest
from plusxy import find_sum

def test_positive():
	assert find_sum(3, 5) == 8

def test_negative():
	assert find_sum(6, -2) == 4

def test_decimal():
	assert find_sum(1.4, 2.2) == 3.6

