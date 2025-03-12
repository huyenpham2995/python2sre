# Question

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

# Thoughts
- There is no way to know if after giving the kid more candy, they will have the most candies, until we know who has the most candies from the beginning
- Need to find the largest number of candies first.
- Then, calculate the current kid's candies after being given extra candies, see if that exceed the largest number of candies.

# BigO
- Time: go through the array twice -> O(2N) -> O(N)
- Space: keep the result array during execution, which has the same number of elements as the candies array -> O(N)