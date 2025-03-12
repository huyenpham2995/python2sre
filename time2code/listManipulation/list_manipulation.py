from collections import defaultdict

def xor_list(a,b):
    res = []
    search = defaultdict(int)
    
    for item in set(a):
        search[item] += 1
    for item in set(b):
        search[item] += 1
    for item, count in search.items():
        if count < 2:
            res.append(item)
    return res     

def and_list(a,b):
    res = []
    search = defaultdict(int)
    
    if len(a)==0 or len(b)==0:
        return []
    
    for item in set(a):
        search[item] += 1
    for item in set(b):
        if search[item] > 0:
            res.append(item)
    return res

def left_list(a,b):
    if len(a)==0:
        return []
    
    res = list(set(a))
    
    for item in set(b):
        if item in res:
            res.remove(item)
    return res
        