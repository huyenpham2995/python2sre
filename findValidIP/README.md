### Question

Input: a file with following content
```
192.87.30.143
143.24.163
159.146,287.89
52.43.110.130
143.14.140.134.123
143.246.43.91
148.252.55.159
190.020.99.96
149.130.0.90
161.133.193.25a
```

Output: valid IPs
```
192.87.30.143
52.43.110.130
143.246.43.91
148.252.55.159
149.130.0.90
```

Note:
1) Please usr RE to implement your solution
2) Leading zeros are not allowed unless the value is 0
3) the file should give you an idea what to watch out for

### Thoughts

Valid IP: there arr 4 groups of numbers in a valid IPv4 (all < 255, no leading 0), same condition
- Just 1 digit, from 0-9
- Or 2 digits, first digit from 1-9 (cant have leading 0), second digit 0-9
- Or 3 digits
    - First digit 1, the last 2 0-9
    - First digit 2, 2nd digit 0-4, third digit 0-9
    - First digit 2, second digit 5, third digit 0-5

### BigO

