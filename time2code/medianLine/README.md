### Question
- You are given a large file which can't fit in RAM. 
- Please create a method to print out the median line. If the median has two lines, print out both lines.

example input: 
```
This is line1
This is line2
This is line3
This is line4
```

example output:
```
This is line2
This is line3
```

### Thoughts
- The point of saying the file cannot fit into RAM means that as we read the file, we cannot store everything.
- There are at most 2 lines that could be the median of the file, so we should only store a limit number of lines for the entire time that we read the file, or know the number of lines.
- If the number of line is odd, there's 1 median line. If it's even there are 2 median lines.
- Since we cannot know if the total number of lines in the file is odd or even until we read the whole file, so we need that first and come back to find the median lines.
- Walkthrough:
    - Line1: median = line1
    - Line2: median = line1 + line2
    - Line3: median = line2
    - Line4: median = line2 + line3
    - Line5: median = line3
    - Line6: median = line3 + line4
    - Line7: median = line4
    - Line8: median = line4 + line5
    - Line9: median = line5
    - Line10: median = line5 + line6
    - Line11: median = line6
    - Line12: median = line6 + line7
    - Line13: median = line7
    - Line14: median = line7 + line8
    - Line15: median = line8
- From the sequence, median line for odd line is ceiling(line#/2), for even line is line#/2 and line#/2+1.

### Pseudocode
- Validate file existence
- Go through the whole files and count the # of lines.
- Read file again and print out the lines at the right position.

### BigO
- Reading time: O(N + N/2) -> O(N)
- Space complexity: O(1)