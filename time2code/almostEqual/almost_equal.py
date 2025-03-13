def is_almost_equal(word1: str, word2: str) -> bool:
    len_diff = abs(len(word1) - len(word2))
    if len_diff > 1:
        return False
    
    c1 = set(word1)
    c2 = set(word2)
    
    char_diff = len(c1.difference(c2))
    if char_diff > 1:
        return False
    if char_diff == 0:
        if len_diff < 1:
            return False
    return True