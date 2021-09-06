import pytest
from romanNumeralsPt3 import romanNumeralsPt3

@pytest.mark.parametrize("input, expected", [(2, "II"),
                                             (9, "IX")])
def testValidInput(input, expected):
    assert romanNumeralsPt3(input) == expected

@pytest.mark.parametrize("input", [0, -10, 2.4])
def testInvalidInput(input):
    with pytest.raises(ValueError):
        romanNumeralsPt3(input)