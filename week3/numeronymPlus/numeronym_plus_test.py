import pytest
from numeronym_plus import verify_numeronym_plus

@pytest.mark.parametrize("input1, input2, expected", [("", "", True), 
                                                      ("a2y", "", False),
                                                      ("i18n", "internationalization", True),
                                                      ("g2o", "gato", True),
                                                      ("y3o", "yoyoyo", False),
                                                      ("ab1c", "bbbc", False),
                                                      ("ab1c", "abc",False),
                                                      ("ab1c", "abcdefgh", False),
                                                      ("ab10c", "abaaaaaaaaaac", True),
                                                      ("ab03c", "abaaac", True),
                                                      ("f1l1ne", "feline", True),
                                                      ("f12l1ne", "feeeeeeeeeeeeline", True),
                                                      ("f12l10ne", "feeeeeeeeeeeeliiiiiiiiiine", True),
                                                      ("f1l1ne", "felne", False),
                                                      ("ab1c", "abcc", True),
                                                      ("2t", "aat", False),
                                                      ("b1", "be", False)])
def test_numeronym_plus(input1, input2, expected):
    assert verify_numeronym_plus(input1, input2) == expected
