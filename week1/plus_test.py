import pytest
from plusxy import findSum

def test_positive():
	assert findSum(3, 5) == 8

def test_negative():
	assert findSum(6, -2) == 4

def test_decimal():
	assert findSum(1.4, 2.2) == 3.6

