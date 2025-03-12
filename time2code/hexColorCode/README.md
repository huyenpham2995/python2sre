### Question
- Input: a file with CSS code
- Output: nothing. Just prin out all the valid hex color code by the order that it appears in the file. Valid hex code requirements are:
   - Starts with # symbol
   - 3 or 6 digit
   - Digit is in the range of 0-9, A-F (or a-f).

### Thoughts
- This is all about regex. Needs to construct a regex so that when the program read each line, extract the one that has the requirements and print it out.

### Pseudocode
- Construct regex string.
- Go through each line, find all string that matches the regex string.
- Print the string

### BigO
O(N)