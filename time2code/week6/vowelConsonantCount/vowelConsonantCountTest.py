import pytest
from vowelConsonantCount import vowelConsonantCount

@pytest.mark.parametrize("input,expected", [("a", (1,0)), ("cat", (1,2)), ("", (0,0))])
def testValidWord(input, expected):
    assert vowelConsonantCount(input) == expected

@pytest.mark.parametrize("input", ["a1", "a2*bc^"])
def testInvalidWord(input):
    with pytest.raises(ValueError):
        vowelConsonantCount(input)

        