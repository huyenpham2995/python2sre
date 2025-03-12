### Question
- Input: log file with content like
```
server1 07-10-2020 disk_usage 90%
server2 07-10-2020 disk_usage 45.5%
server3 07-10-2020 disk_usage 65%
server4 07-10-2020 disk_usage 23.5%
server5 07-10-2020 disk_usage 96.5%
```
- Output: print out names of servers and its disk_usage whose disk_usage is over 85%
```
server1 90%
server5 96.5%
```
- Note: the percentages can be integer (e.g. 50%) or a decimal number with one fraction digit (e.g. 45.5%)

### Thoughts
- Do we assume that the lines are all formatted correctly? (if not just throw error). What can go wrong:
   - Line is not in correct format: serverName date "disk_usage" percentage
   - The percentage <0 or >100

### Pseudocode
- Loop through each line.
   - Split line by space
   - If the line has one of the errors above, throw error
   - Capture 1st element as name. Remove last character from the last element (the % in percentage) and convert that to float (call X). If it is valid (0 <= X <= 100) and X > 85 => print.

### BigO
O(N)