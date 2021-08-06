### Question
An upgraded version of numeronym. Validate is a word matches the provided numeronym. Numeronym can be invalid (does not start or end with letters), empty or there are multiple numbers in between. Numeronym can also have start/end with multiple letters (not necessary just one letter)
- ga1o - gato -> true!
- f1l1ne - feline -> true!
- 2t - cat -> false! (invalid)

### Thoughts
- Input and output:
    - Input: numeronym (string) and the word (string)
    - Output: boolean
- Since numeronym does not neccessary have to start and end with only 1 letter, the method to convert the middle part to integer is not working => has to travel the numeronym character by character, and determine on the go.
    - Travel through the numeronym
        - If the current character is a letter, compare the letter of the numeronym to the letter of the word.
        - If the current character is a number, grab all the number that goes together consecutively. 
            - For example: "a123b", we detect 1, then keep going until there's no number anymore (keep the numbers in `expectedLength`). Then convert that `expectedLength` into a string. In this example, `expectedLength = 123`
            - If the length of `word` from current position to the end is less than the `expectedLength`, i.e it does not match => return False
    - When we traverse through every character of the `numerynom` but we have not reached the end of `word`, i.e `word` is longer than `numerynom` => return False
    - When we have reached the end, everything passed => return True
- Edge case(s):
    - When both word and numeronym are "", return True
    - When word is "" but numeronym is not (and vice versa), return False
    - When numeronym does not begin or end with a letter, return False (invalid)