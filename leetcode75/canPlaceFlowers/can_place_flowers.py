from typing import List

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    for i in range(0,len(flowerbed)):
        if flowerbed[i] == 1:
            continue
        if (i-1 < 0 or flowerbed[i-1]==0) and (i+1 >= len(flowerbed) or flowerbed[i+1]==0):
            flowerbed[i] = 1
            n-=1
    return n<=0