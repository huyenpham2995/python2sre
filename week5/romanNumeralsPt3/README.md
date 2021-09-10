### Questions
- Give me a program which can turn numbers into strings! (ie 2-> II)

### Thoughts
- Input and output:
    - Input: an integer
    - Output: a string represent its roman numeral form.
- There are some default values for roman numerals (I=1, V=5. etc).
- Look at the largest value in the default values that is smaller than the number that I need to convert. Subtract that number from the actual number. Keep doing that until the actual number is 0. Example: 19
    - Does 19>=1. Yes. Move on
    - Does 19>=4. Yes. Move on
    - Does 19>=5. Yes. Move on
    - Does 19>=9. Yes. Move on
    - Does 19>=10. Yes. Move on
    - Does 19>40. No. Go back!
    - The closest number to 19 that is smaller than 19 is 10. Subtract 10 from 19 (9 left), result = X
    - Does 9>=1. Yes. Move on
    - Does 9>=4. Yes. Move on
    - Does 9>=5. Yes. Move on
    - Does 9>=9. Yes. Move on
    - Does 9>10. No. Go back!
    - The closest number to 9 that is smaller than 9 is 9. Subtract 9 from 9 (0 left), result = XIX
    - Now actual number = 0. Stop
- Special case:
    - If input is not a positive integer or not an integer => exception!

### Pseudocode
1. Create a dictionary with all the default values.
2. Throw exception if input is not a positive integer or not an integer.
3. Create a loop and terminate when input is 0:
    - Find the closest number in the default dictionary to input that is smaller than input.
    - Subtract that number from input.
    - Appending the string represent that number to result.
4. Return result

### BigO (not sure)
- Worst case scenerio going through the same time as the value of the input => time complexity O(num).
- Both dictionary and values array have a fixed size => space complexity O(1).