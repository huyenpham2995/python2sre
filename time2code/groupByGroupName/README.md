### Question
Input: the name of an inout file with following content: username groupname userid homepath
Output: a new file sorted by groupname alphabetically

Note: there's a command line to do this "sort -t' ' -k2 filename", but we want you to do this in programming languages

### Thoughts
- Will the filename be valid?
    - Yes, continue
    - No. throw error
- Read the content of each line of the input file into a dictionary. The value will be the array of the line being split by white space. If the array length != 4, abort, since this input is faulty (for example, if the line only has 3 fields, we don't know which one is the groupname).
- Sort the dictionary by key
- What if the group name are the same?
    - Sort by the next element, which is username, because there's a very high chance username is unique.

### Pseudocode
1. Try to open the file with file name. If not valid -> abort.
2. Read the file\
    2.1. At each line, split the line with space a delim (this will be an array). If array length != 4 -> throw exception.\
    2.2. If array length == 4, add an entry to the dictionary with the 2nd element (groupname) as key and the value is an array of array (line after being split).\
3. Sort the dictionary by key
4. Loop through all elements of the dictionary:\
    4.1. If a key contains multiple value, sort by 3rd element (username)\
    4.2. Join the array by space and write to output file.

### BigO
- Read each line into dictionary: O(N)
- Sort dictionary: O(NlogN)
- Loop through dictionary and write the lines to output file: O(N)
=> Overall O(NlogN)