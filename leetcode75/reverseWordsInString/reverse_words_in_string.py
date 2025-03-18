def reverse_words(s: str) -> str:
    if s == "":
        return ""
    
    s = s.strip().rstrip()
    words = s.split()
    res = ""

    for i in range (len(words)-1, 0, -1):
        res += words[i] + " "
    return res + words[0]