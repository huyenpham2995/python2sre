import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("input,expected", [(9, "fizz"),
                                            (-3, "fizz"),
                                            (5, "buzz"),
                                            (-10.0, "buzz"),
                                            (15, "fizzbuzz"),
                                            (0, "fizzbuzz"),
                                            (1.234, 1.234),
                                            (-2.222, -2.222)])
def testValidInput(input, expected):
    assert fizzbuzz(input) == expected

@pytest.mark.parametrize("input", ["abc", ""])
def testInvalidInput(input):
    with pytest.raises(ValueError):
        fizzbuzz(input)
