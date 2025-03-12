import pytest
from bubbleSort import bubbleSort

@pytest.mark.parametrize("l,sorted_l", [([8,1,6,3,9,7], [1,3,6,7,8,9]),
                                      ([],[]),
                                      ([1,2,3,4,5], [1,2,3,4,5])])
def testValidInput(l, sorted_l):
    assert bubbleSort(l) == sorted_l

@pytest.mark.parametrize("l", [1, "invalid"])
def testInvalidInput(l):
    with pytest.raises(TypeError):
        bubbleSort(l)