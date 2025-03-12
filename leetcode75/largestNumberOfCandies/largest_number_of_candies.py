def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    largest = max(candies)
    res = []

    for candy in candies:
        if candy + extraCandies >= largest:
            res.append(True)
        else:
            res.append(False)
    return res