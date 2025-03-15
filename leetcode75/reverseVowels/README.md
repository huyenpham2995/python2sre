# Question
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

# Thoughts
- Vowels are 'a', 'e', 'i', 'o', and 'u'
- The reverse of the string is basically the beginner letters swapped with the end letters.
- Can go 2 ways: 1 pointer go from the beginning, one from the end
    - The characters can only be swapped if they are both vowels. Once they are swapped, both pointers move on
    - If the beginner pointer points to a vowels, keep it position, else keeps moving forward
    - If the end pointer points to a vowels, keep it position, else keeps moving backward
    - We end analyzing the string when both pointers meet each other in the meeting ( we have scanned through the whole string)

# BigO

- Space: keep an array of characters of the string + 2 pointers -> O(N)
- Time: 
    - We iterate from both front and back of the string and stop when they meet each other in the "middle" -> go through each character once -> O(N)
    - Each time we iterate, there's a step to see if the character is in the list of vowels. There are 5 vowels, so the time to check is O(5*N) -> O(N)