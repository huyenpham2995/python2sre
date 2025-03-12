### Question
- https://www.hackerrank.com/challenges/piling-up/problem

### Thoughts
- Basically the largest number has to be at the base, and only grab the most far left or the most far right number at a time. If we make it to all the numbers in the array, the answer is Yes.
- Need to keep track of the number at the "base", since the next number needs to be smaller or equal than that base number.
- Once the number is processed, pop it out of the array.

### BigO
- Time Comlexity: each iteration we eliminate at least 1 number in the array. Worst case is going through all numbers (since it can be piled up) -> O(N)
- Space Complexity: only store base and comparing first and last number, modify the original array -> O(1). If we don't want to modify the original array and decide to make a copy of it, then space is O(N)