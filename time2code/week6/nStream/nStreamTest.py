import pytest
from nStream import nStream
from nStreamTwist import nStreamTwist

@pytest.mark.parametrize("l,N,output", [(["a","b","c","d","e"],3,[["a","d"],["b","e"],["c"]]),
                                        (["a"],2,[["a"],[]]),
                                        ([],5,[[],[],[],[],[]])])
def testValidInput(l,N,output):
    assert nStream(l,N) == output
    assert nStreamTwist(l,N) == output

@pytest.mark.parametrize("l,N", [(["a","b","c","d","e"],-1),
                                 (["a","b"],0),
                                 (["a","b"],1.5)])
def testInvalidInput(l,N):
    with pytest.raises(Exception):
        nStream(l,N)
        nStreamTwist(l,N)
