import pytest
from roman_numerals_pt3 import roman_numerals_pt3

@pytest.mark.parametrize("input, expected", [(2, "II"),
                                             (9, "IX"),
                                             (19, "XIX"),
                                             (137, "CXXXVII")])
def test_valid_input(input, expected):
    assert roman_numerals_pt3(input) == expected

@pytest.mark.parametrize("input", [0, -10, 2.4])
def test_invalid_input(input):
    with pytest.raises(TypeError):
        roman_numerals_pt3(input)