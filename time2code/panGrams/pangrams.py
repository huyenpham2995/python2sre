def is_pangrams(s: str) -> str:
    check_alphabet = {}
    
    for c in s.lower():
        if c.isalpha():
            check_alphabet[c] = 1
        if len(check_alphabet) == 26:
            return "pangram"
    
    return "not pangram"
        