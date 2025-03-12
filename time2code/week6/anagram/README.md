### Question
- Given two words, tell me if one is an anagram of the other. Examples: 
    - cats, tacs => true
    - fast, fats => true

### Thoughts
- Input and output:
    - Input: 2 strings
    - Output: boolean
- Two words are anagram if they have the same letters but just in different order, which means they have the same count for each letter.
- Example: cats, tacs
    - We look at "cats", which has c,a,t,s
    - Looking at "tacs", theres t,a,c,s
    - Since we don't care about the order but just the same amount of letters, the letters are the same.
    => "cats" and "tacs" are anagram.

### Pseudocode
1. Create 2 dictionaries, each with one word to keep track of the letters and the number that each letter appear in the words.
2. Comparing 2 dictionaries, if each entries have the same count then return True, else False.

### BigO
- Going through each word once to create the dictionary. Going through both dictonary once to check the number of time each char appears and compares to the other string => time complexity O(N) (N is the length of word).
- Having 2 dictionaries to store the characters of both words => space complexity O(2N) -> O(N).