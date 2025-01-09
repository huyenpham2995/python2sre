### Question
- Input: a .py file wich contains comments.
- Output: a .py file with all comments removed.

### Thoughts
*   Throw error if file does not exist
*   There are 2 types of comments: line (#) and block (""")
    *   For the line comment, just need to ignore the line that starts with #
    *   For block comment, have to keep track of where the comment starts and ends. When detects """ for the first time, keep ignoring the consequence lines until hitting the 2nd triple quote. We need a boolean flag with this, the flag starts at False.
        *   It gets trickier as the triple quote might not stand alone in the line. Technically something like this can happen: 
            *   """test""". 
            *   """test
                """
            *   """
                test"""
        *   So instead of finding if the line is """, we need to detect if it starts/ends with """
            *   If it is, check to see how many """ there are
                *   If there's odd number, of """, flip the flag to its opposite value.
                *   If there's even number, don't flip the flag (because technically we flip the flag for the even number of times, which returns to the original state).
        *   We will only count the line as valid if:
            *   Line does not start or end with """
            *   The flag at the time is False.
            *   We do preserve empty line.

### Pseudocode
1.  Create an array to store the valid lines. Create a boolean falg to keep track of """. Boolean sets to False.
2.  Open file with try-except to make sure it is valid.
3.  Read each line of file\
    3.1.    If line starts or ends with """
        3.1.1.  If there are odd number of """ in the line, set boolean flag to its negate value.\
    3.2.    Else if boolean is False and the line does not start with #, add the line into the valid lines array
4.  Write the valid array to the output file

### BigO
Go through the file once and process in place => O(N).