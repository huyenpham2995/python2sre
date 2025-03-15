def reverse_vowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = list(s)
    i = 0
    j = len(s) - 1
    
    while i <= j:
        if res[i].lower() in vowels and res[j].lower() in vowels:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        else:
            if res[i].lower() not in vowels:
                i+=1
            if res[j].lower() not in vowels:
                j-=1
    return ''.join(res)