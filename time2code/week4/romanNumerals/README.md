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
1. Create a dictionary of roman numerals.
2. Check to see if the string is empty, if it is then invalid, return None
3. Go through each character in the string, convert them to uppercase:
    - If the letter does not exist in the dictionary, that's invalid => None
    - If current roman numerals value >= the previous one, just add it to the result sum.
    - If current roman numerals value < the previous one
        - Deduct the previous value from the sum (reset sum) to avoid it is being considered twice.
        - Take the current value - previous value (eg: IV = 5 - 1 = 4)
        - Add that value just calculated to the sum (sum = sum + 4)
    - Update index.

### BigO
- Go through the string once => Time complexity O(N) (N being the length of the string).
- Have a dictionary of a fixed size for roman numerals, only keeping track of 2 value at the same time (current and previous value) => space complexity O(1).
