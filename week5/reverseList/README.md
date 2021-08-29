### Question
- Reverse a list

### Thoughts
- Input and output:
    - Input: a list of anything (int, string).
    - Output: the reverse list of the input
- Example: [1,2,3,4] -> [4,3,2,1]
- The first element becomes the last one, the 2nd one becomes the 2nd to the last and so on.
- Can go through the list from the end to the beginning, append each element to a new list and return that new list.
- Since the 1st become the last, I can actually swap their position. Same thing goes to 2nd and 2nd to the last, etc. No new list needs to be created. Done with the swap when element(s) in the middle of list are swapped.

### Pseudocode
1. Having 2 variables to keep track of the start and end index
2. Swap the elements at the 2 current indexes.

### BigO

