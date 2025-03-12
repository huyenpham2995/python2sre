def merge_alternately(word1: str, word2: str) -> str:
    if len(word1) < 1:
        return word2
    if len(word2) < 1:
        return word1

    res = ""
    i = 0

    while i < len(word1) and i < len(word2):
        res += word1[i]
        res += word2[i]
        i += 1
    
    if i < len(word1):
        res += word1[i:]
    if i < len(word2):
        res += word2[i:]

    return res