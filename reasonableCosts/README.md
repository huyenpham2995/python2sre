### Question

- Input: given a file with the following content
```
Date City Cost Recommended
05/14/20 Hualpen $14.71 Yes
10/17/19 Khairpur $26.25 No
10/13/20 Biercze $3.50 No
03/12/20 Carleton $85.83 No
03/04/20 Putaendo $80.65 No
08/24/21 Curacautín $46.89 Yes
04/22/20 Aklavik $90.95 Yes
10/28/19 Heusden $41.67 Yes
12/30/19 Duns $19.00 No
12/14/20 Gilgit $65.35 Yes
08/28/19 Greymouth $91.52 No
04/04/20 Sohbatpur $53.49 No
02/14/20 Villavicencio $33.59 No
09/09/20 Sevsk $76.03 Yes
01/30/21 Corroy-le-Chteau $80.44 Yes
03/17/21 Brugge $19.70 Yes
09/09/19 Raychikhinsk $71.07 No
09/10/20 Naarden $31.06 Yes
07/13/21 Lauco $75.97 Yes
11/22/19 Marentino $95.26 No
10/17/19 Nuragus $99.34 No
```

- Output: the lines sorted by date where cost is between $20 and $50, and recommended is Yes

### Thoughts
- Read each line, convert the money to float and only keep the lines that satisfy the condition, then sort the list of qualified lines by dates.

### BigO
- Time Complexity: read through all lines O(N), sort by date O(NlogN) -> O(NlogN)
- Space Complexity: at most O(N) (if all lines qualified)