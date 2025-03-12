### Question
Validate is a word matches the provided numeronym. In this simple version, assume numerynom will start and end with a character
The middle part of the numerynom will be digits
- a11y - accessibility -> True
- i18n -internationalization
- c1t - cat
- g2o - gato
- f4e- feline

### Thoughts
- Input and output:
    - Input: numeronym (string) and the word (string)
    - Output: boolean
- The first and the last element of the numeronym will be a character, so we know that from
index 1 to n-2 (n being the length of the string) it will contain numbers.
- There are 2 steps that we need to do:
    - Verify the first and last character of the word match the first and last character of the numeronym.
    - Verify there are X characters between word[1] and word[n-2], where X is int(numeronym[1:n-1]).
- Edge case(s):
    - When word is "", return False

### Pseudocode
- If word is "" return False
- If both of them are not ""
    - Check to see if first and last characters of numeronym match with first and last characters of word.
        - If match:
            - Convert the numeronym (excluding the first and last characters) into int => expected length from word
            - Check to see if the length of word (excluding the first and last characters) is the same with the expected length
        - If not, return False

### BigO
- Time complexity: only 1 if statement to compare the beginning and the end character of word and numeronym => O(1)
- Space complexity: no extra space used => O(1)
    
