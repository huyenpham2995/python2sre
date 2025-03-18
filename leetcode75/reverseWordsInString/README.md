# Question
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75 

# Thoughts
- The string might contain more than 1 space between the words, and the result can only return 1 space between each word.
    - To avoid leading and trailer spaces, remove those first
    - The split() function will remove all spaces in between.
- Solution 1: After splitting the string into list of words, go backwards and concatenate the words to make the result string
    - Append a space after every words, except for the last one (i.e the first word in the list).
- Solution 2: 2 pointers, one go forward and one go backwards, switch positions of the words during traverse

# BigO
- Space: store a list of each word -> O(N)
- Time: Go through each word once -> O(N)