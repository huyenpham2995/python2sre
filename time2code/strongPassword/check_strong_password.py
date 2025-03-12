import re

def strongPassword(n,pw):
    missing_char = 6-n if (6-n)>0 else 0
    missing_others = 0
    
    
    if not re.search(r"[0-9]",pw):
        missing_others += 1
    if not re.search(r"[A-Z]",pw):
        missing_others += 1
    if not re.search(r"[a-z]",pw):
        missing_others += 1
    if not re.search(r"[!@#$%^&*()-+]",pw):
        missing_others += 1
    
    return max(missing_char,missing_others)