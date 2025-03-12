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
- If there's no parenthesis in the string, it's also valid.

### Pseudocode
1. Go through the string and extract only the parenthesis to a list.
2. If the length of the parenthesis list is odd then return False, since the parenthesis are imbalance. 
3. Keep track of the current and previous parenthesis in the list. 
    - If a ) is detected:
        - If it is at the beginning of the list, return False.
        - Else pop that and the previous one out of the list (we know the previous one is an open parenthesis. Update the current index to the previous position (since we pop out the previous parenthesis as well).
    - If it's a (, update the index and continue.
    - When finish traversing the parenthesis list, if there's still parenthesis left, then that's imbalance => False. Eg: [(,(,(]. If it's empty so they are balance.

### BigO
- Go through the string 2 times (one for extracting the parenthesis, one for analyze the parenthesis in the list), so time complexity O(N) (N is the lenght of the string).
- Have a list to keep track of all parenthesis. In the worst case scenerio the entire string contains only parenthesis => space complexity O(N).