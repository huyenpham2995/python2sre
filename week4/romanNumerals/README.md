### Question
- Convert the Roman numberals string to number
    - LV - 55
    - CL  - 150
    - CXXXVII - 137

### Thoughts
- Input and output:
    - Input: the roman numerals string.
    - Output: an int corresonds to the roman numerals string.
- Each character stands for a number. Need a dictionary to look up the character to number.
- From left to right, can traverse the string and for each character add up the value of it then return the sum.
- The not simple case being something like "IX" or "IV", they are 9 and 4 (not 11 and 6) so cannot take the sum of them like that. For those cases, the previous character has smaller value than the current one. Will need to keep track these 2 positions, if the value at string[prev] is less than the value at string[cur], then it's string[cur] - string[pre] and add that value to the current sum.
- Special case: 
    - If the input is in lowercases, it's still valid.
    - If the input contains a letter/character that does not have any value in roman numerals dictionary, that's an invalid string.

### Pseudocode

### BigO
