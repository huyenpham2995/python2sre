### Question
- https://www.hackerrank.com/challenges/pangrams/problem

### Thoughts
- Keep a dictionary of all the letters that appear in the string. If at the end, the length of the dictionary added up to 26, return "pangram", else "not pangram".
- There will be a mix of lowercase and uppercase, and they are counted the same, so before doing the count, just convert the whole string to lowercase.
- Have to remove any special character out of the count.
- The moment the length of the dictionary reaches 26, terminate without reading the whole string.

### BigO
- Time complexity: at most, we will go through every characters (in the case it is not pangram) -> O(N)
- Space complexity: at most, we are storing a dictionary of 26 characters -> O(1)
