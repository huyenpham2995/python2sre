### Question
- Strong password criteria
    - Its length is at least 6.
    - It contains at least one digit.
    - It contains at least one lowercase English character.
    - It contains at least one uppecase English character.
    - It contains at least one special character. The special characters are: !@#$%^&*()-+
- Output: the minimum number of characters to add to get the strong password

### Thoughts
- Input (n, password), where n is the length of the password.
- This will be a bunch of regex checking and flags.
- Right off the bat, the number of missing characters is 6-n. So the first flag is missing_char = 6-n. 
    - if n>6, missing_char is 0. Else it will just be 6-n
- 2nd flag is missing_digit. If pw contains digit, then missing_digit is 0, else 1
- 3rd flag is missing_lower (lowercase English letter). Same logic as above
- 4th flag is missing_upper (uppercase English letter). Same logic as above
- 5th flag is missing_special. Same logic as above
- Now the missing characters could be overlapped with one of the missing_* above. So instead of summing all of them up, it would be the larger value of the 2: either missing_char or the sum of flag 2-5, whichever larger.

### Pseudocode
- missing_char = 6-n. If missing_char < 0, missing_char = 0
- Find all digits in the pw. If the result < 1, missing_digit = 1
- Find all lowercase characters in the pw. If the result < 1, missing_lower = 1
- Find all uppercase in the pw. If the result < 1, missing_upper = 1
- Find all special characters in the pw. If the result < 1, missing_special = 1
- Return max(missing_char, missing_digit+missing_lower+missing_upper+missing_special)

### BigO
- Go through the whole password 4 times => O(4N) => O(N)
