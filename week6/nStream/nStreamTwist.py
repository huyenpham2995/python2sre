def nStreamTwist(l,N):
    # invalid input
    if N < 0 or not isinstance(N, int):
        raise Exception("N has to be a positive integer")
    
    # create N empty list
    result = []
    for _ in range(N):
        result.append([])
    
    # add each item to their bucket based on their position
    currentIndex = 0
    for item in l:
        pos = currentIndex%N
        result[pos].append(item)
        currentIndex += 1

    return result