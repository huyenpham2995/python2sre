### Question
- Reverse an integer
    - 1245	-> 5421
    - 1,245 -> 2,542
    - 3,200 -> 23

### Thoughts
- Input and output:
    - Input: an integer in the form of a string.
    - Output: the reverse of that integer, also a string.
- If input is empty, there's nothing to do, just return it.
- For a normal string like "1234", can just traverse from the end of the string, create a new string and return that.
- That won't work with string that contains comma, since "1,234" will become "432,1". The position of the comma still needs to be in second place. Can still traverse from the end of the string, has a flag to keep track if the string has comma. When we reach the first number, put the comma back to the orignal location.
- The above again will be invalid for something that ends with zero(s). "3,200" will become "23" without the zeros and no comma. Comma is a mark for the thousandth, so every 3 numbers there will be a comma. Still traversing the original string from the end, then convert it into an int (to eliminate the zeros in the front), then insert the comma for every 3 numbers (if the original string has commas). To know how many comma to insert, take the length of the string after reversing and divde by 3.

### Pseudocode
1. If string is empty, return string.
2. Traverse the original string in reverse order:
    - If a comma is detected, flip the flag to True.
    - Else it's a number, just add to the result.
3. Convert the result into an int to eliminate the 0(s) if any, then convert it back to a string.
4. Add back the comma(s):
    - If result string is less than 4 digits, no comma needed.
    - Adding the comma for every 3 digit, starting from the end of result string.

### BigO
- Traverse the orignal string => time complexity O(N) (N being the length of the original string).
- Create the result string. In the longest case scenerio, the result string has the same length with the original string => space complexity O(N).