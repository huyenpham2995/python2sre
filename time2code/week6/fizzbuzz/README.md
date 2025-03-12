### Question
- If divisible by 3, print fizz
- If divisible by 5, print buzz
- Otherwise number only plz

### Thoughts
- Input an Output:
    - Input: a number (int/float).
    - Output: fizz/buzz/frizzbuzz/the number itself.
- Take in the number and try to divide to 3: if remainder = 0 print fizz.
- Divided by 5, if remainder = 0 print buzz.
- Negative and decimal numbers count.
- Special case: 
    - What if it is divided to both 3 and 5? frizzbuzz
    - What if the input is not a number but string(regular or empty string)? Exception!
- Else return itself

### Pseudocode
1. Test to see if it is really a number
    - If not raise exception
2. Divide by 3
3. Divide by 5
4. Return keywors or itself

### BigO
- No loop, only going through some if statement with a number => time complexity O(1).
- Keep track of the number and result => space complexity O(1)