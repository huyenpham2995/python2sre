import pytest
from anagram import verifyAnagram

@pytest.mark.parametrize("input1, input2, expected", [("cats","tacs",True),
                                                      ("fast","fats",True),
                                                      ("var1","ra1v",True),
                                                      ("abcd","cdeab",False),
                                                      ("abcd", "adec",False)])
def testValidInput(input1, input2, expected):
    assert verifyAnagram(input1, input2) == expected