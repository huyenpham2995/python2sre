### Question
- Validate the parentheses 
    - ( ) => True
    - ( )  ) => False
    - Sometimes I will use a parenthesis in a string

### Thoughts
- Input and output:
    - Input: a string with (or without parenthesis)
    - Output: boolean
- Keeping a list of only the parenthesis. 
    - An open parenthesis can be followed by either open or close parenthesis.
    - A close parenthesis needs to have an open parenthesis before it.
- If the character is not ( or ), then skip it.

### Pseudocode

### BigO