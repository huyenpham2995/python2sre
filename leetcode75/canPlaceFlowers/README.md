# Question
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

# Thoughts
- If n = 0, which means no flower needs to be placed, always return True
- The flower can only be placed if
    - The slot does not have flower yet
    - There's nothing on the left or the left of the current slot does not have flower, and there's nothing on the right or the right of the current slot does not have flower.
- Wherever you can put a flower, put it down for the next iteration

# BigO

- Space: iterating through the array of flowerbed -> O(N)
- Time: go through each slot in the flowerbed once -> O(N)