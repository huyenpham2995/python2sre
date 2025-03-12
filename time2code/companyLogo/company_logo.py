from collections import defaultdict

def company_logo(logo: str):
    # key: character, value: its appearance
    char_count = defaultdict(int)
    
    # key: # of appearance, value: array of characters with that # of appearance
    rev_char_count = defaultdict(list)
    res = []
    
    for char in logo:
        char_count[char] +=1   
    for key, val in char_count.items():
        rev_char_count[val].append(key)
    
    # Sort by num of appearance
    for num_appearance, chars in sorted(rev_char_count.items(),key=lambda x:x[0], reverse=True):
        # Sort letters with the same # of appearance
        for char in sorted(chars):
            if len(res) == 3:
                break
            res.append((char,num_appearance))
    return res
