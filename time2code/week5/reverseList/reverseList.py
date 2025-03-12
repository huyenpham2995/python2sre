def reverseListOne(l: list) -> list:
    if len(l) < 2:
        return l
    
    result = l[::-1]
    return result

def reverseListTwo(l: list) -> list:
    if len(l) < 2:
        return l

    firstIndex = 0
    lastIndex = len(l) - 1

    while firstIndex < lastIndex:
        temp = l[firstIndex]
        l[firstIndex] = l[lastIndex]
        l[lastIndex] = temp
        firstIndex += 1
        lastIndex -= 1

    return l