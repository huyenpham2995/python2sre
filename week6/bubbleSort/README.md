### Question
Implement bubble sort (i.e adjacent sort)

### Thoughts
- Input and output:
    - Input: an unsorted list
    - Output: a sorted list
- How bubble sort work: comparing 2 elements next to each other, if the current > next one => swap. Bubbling up - the largest element will get to the end of the list after each round.
- Example: [8,1,6,3,9,7]
    - Round 1:
        - currentIndex = 0: 8>1 -> [1,8,6,3,9,7]
        - currentIndex = 1: 8>6 -> [1,6,8,3,9,7]
        - currentIndex = 2: 8>3 -> [1,6,3,8,9,7]
        - currentIndex = 3: 8<9 -> [1,6,3,8,9,7]
        - currentIndex = 4: 9>7 -> [1,6,3,8,7,9] -> the largest number 9 is at the end.
        - Reset currentIndex.
    - Round 2:
        - currentIndex = 0: 1<6 -> [1,6,3,8,7,9]
        - currentIndex = 1: 6>3 -> [1,3,6,8,7,9]
        - currentIndex = 2: 6<8 -> [1,3,6,8,7,9]
        - currentIndex = 3: 8>7 -> [1,3,6,7,8,9] -> the 2nd largest number is 8.
        - Reset currentIndex.
    - Round 3:
        - currentIndex = 0: 1<3 -> [1,3,6,7,8,9]
        - currentIndex = 1: 3<6 -> [1,3,6,7,8,9]
        - currentIndex = 2: 6<7 -> [1,3,6,7,8,9]
        - Reset currentIndex.
    - Round 4:
        - currentIndex = 0: 1<3 -> [1,3,6,7,8,9]
        - currentIndex = 1: 3<6 -> [1,3,6,7,8,9]
        - Reset currentIndex.
    - Round 5:
        - currentIndex = 0: 1<3 -> [1,3,6,7,8,9]
    - Return sorted list [1,3,6,7,8,9]
- Edge case:
    - If list is empty -> return empty list
    - If input is not a list -> exception!

### Pseudocode
1. If list is empty returns empty list
2. If input is not a list -> raise TypeError (exception)
3. Go through each element in the list
    - Compare the value at current index with the next one until the end (the next round we don't need to check the end of the previous round, since the largest value possible in that position is already bubbled there)
        - If curr < next -> swap (curr, next)
        - Else increasing current value until the end.
    - Reset current index to 0.
4. Return result list

### BigO
- Nested loop to go through the list => time complexity O(n^2) (n is the length of the list).
- Space complexity: operation on the original list => space complexity O(1)