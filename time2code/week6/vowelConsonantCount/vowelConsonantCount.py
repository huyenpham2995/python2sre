def vowelConsonantCount(s: str) -> ():
    vowels = ["a","e","i","o","u"]
    vowel = 0
    consonant = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel += 1
            else:
                consonant += 1
        else:
            raise ValueError("Input should only contain letters")

    return (vowel, consonant)

