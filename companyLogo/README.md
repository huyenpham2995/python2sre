
### Question

https://www.hackerrank.com/challenges/most-commons/problem

### Thoughts
- Need to know how many of each character in the string is. Can go through it then count.
- After that, go through each character and sort them by their appearance. For characters that have same amount of appearance, sort them by alphabetical order.
- Go through the sorted list (in reverse order, i.e from large to small # of appearances) until there's enough 3 characters.

### BigO
- Go through the whole string to count character O(N)
- Sort by # of appearance: there are 26 characters. At most, we are going to sort the appearance of these 26 characters => O(1)
- Space: 2 dictionaries of at most size 26 => O(1)
