def nStream(l: [], N: int) -> []:
    # invalid input
    if N < 0 or not isinstance(N, int):
        raise Exception("N has to be a positive integer")

    #handle empty master list
    result = []
    if len(l) == 0:
        for _ in range(N):
            result.append([])
        return result

    minItems = int(len(l)/N)
    currentIndex = 0
    group = 0

    while group < N and currentIndex < len(l):
        result.append(l[currentIndex:currentIndex+minItems])
        currentIndex += minItems
        group += 1

    # having lefftover
    while currentIndex < len(l):
        pos = currentIndex % N
        result[pos].append(l[currentIndex])
        currentIndex += 1

    return result

print(nStream([],3))