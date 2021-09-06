### Question
- Roman numerals can now follow the format IC(99) or XVIC(84) 

### Thoughts
- Input and output:
    - Input: a string for roman numeral.
    - Output: integer represents roman numeral.
- Read through the string from left to right. If the next character value is less than the previous char value, just adding their values together. Eg: XVI
    - We see X first, add X to the sum (sum = 10).
    - We see V next. V < X, V < sum => add V to the sum (sum = 10+5 = 15).
    - We see I next. I < X, I < sum => add I to the sum (sum = 15+1 = 16).
    - Return 16.
- There are 2 cases where we need to deduct:
    - If the current char value > the previous char value (XIV) => cur char - previous char. Eg: XIV.
        - We see X, add it to sum (sum = 10).
        - We see I, I < X => add I to sum (sum = 11).
        - We see V, V > I:
            - V - I = 4. Add this value to sum (sum = 11+4 = 15)
            - Deduct I from the sum so we don't count for it twice (sum = 15-1 = 14).
        - Return 14
    - If the current sum is less than the next char value => cur char - current sum. (IVX)
        - We see I, add it to sum (sum = 1).
        - We see V, V > sum:
            - V - sum = 5-1 = 4. Add this value to sum (sum = 4+1 = 5).
            - Deduct I from the sum so we don't count for it twice (sum = 5-1 = 4).
        - We see X, X > sum:
            - X - sum = 10-4 = 6. Add this value to sum (sum = 6+4 = 10).
            - Deduct IV from sum so we don't count for it twice (sum = 10-4 = 6).
        - Return 6.

### Pseudocode
1. Traverse each character in the string from left to right.
2. First character is added automatically to the result sum.
3. Compares the current char to the previous char:
    - If current char < previous char: just add current char value to the sum
    - Else:
        - If current char > result sum: new result sum = current char value - result sum.
        - Else if current char > previous char:
            - Deduct previous char from result (so we don't take into account the previous char twice).
            - result = result + current char - previous char
4. Update index position and repeat step 3 until reaching the end of the string.

### BigO
- We traverse the string once => time complexity O(N) (N is the length of the input).
- Only use 2 variable to keep track of the value of current and previous characters, 1 more to keep track of the current index => space complexity O(1).