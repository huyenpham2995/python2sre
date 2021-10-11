### Question
- Write a program to test to see if a json file is properly formatted

### Thoughts
- Input and output:
    - Input: a json file.
    - Output: a boolean (True if it's properly formatted, false otherwise)
- What to check?
    - json file contains a lot of parenthesis => Check for valid parenthesis
        - `{}`, `()`, `[]`, `""`. Any parenthesis inside "" (quotation) should be ignored
        - The json key and value are separated by `:` 
    - Each object in the json file are separated by `,`
    - Any special symbol after `\` (escape) should be ignored 

### Pseudocode

### BigO
