def bubbleSort(l: list) -> list:
    if not isinstance(l, list):
        raise TypeError("Expected a list")

    # controlling where the inner loop should stop
    for endIndex in range(len(l)):
        # controlling current position
        for currentIndex in range(len(l)-endIndex-1):
            if l[currentIndex] > l[currentIndex+1]:
                # swap
                temp = l[currentIndex+1]
                l[currentIndex+1] = l[currentIndex]
                l[currentIndex] = temp
    
    return l