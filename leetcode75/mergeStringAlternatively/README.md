# Question

https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75 

# Thoughts
- If one word is empty, returns the other word
- Alternatively insert a character from word1, then word2, then so on. The character being inserted at each time is at the same position for each word
- If a word is shorter, the rest of the characters of the other word is append to the result.

# BigO

Let length of word1 be N and word2 be M
- Time: go through all characters of both word to construct the result => O(N+M)
- Space: the result will have the length N+M.