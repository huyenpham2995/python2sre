### Question
- Given a word, tell me the vowel and consonant count

### Thoughts
- Input and output:
    - Input: a string.
    - Output: a tuple of 2 elements: the count of vowel and consonant in the string.
- Vowels: a,e,i,o,u.
- Consonant: the rest.
- Look at the string one by one. If it's either a,e,i,o,u then +1 to vowel. If not in the list then +1 to cosonant.
- Special case: what if the word does not contain only letters? What if there's numbers andd special symbols? Raise exceptions!!

### Pseudocode
1. Traverse the string character by character
    - If it's either a,e,i,o,u, vowel +1.
    - Else:
        - If it's alphabet character then +1 consonant.
        - If it's another type of characters (digit, special character), raise exception (we need a word with all alphabetical characters).
2. Return a tuple of (vowel, tuple).

### BigO
- Traverse the string once => time complexity O(N) (N is the length of the string).
- Only keep track of 2 vars vowel and cosonant => space complexity O(1)