### Question
- Given a list of strings, create a list of mostly of N streams.
    - ie turn a list of 10 strings, into N(5) lists
- SUPER MEAN TWIST - you must split evenlyish, but can't keep count of output array size and can't use the size of the list.

### Thoughts
- Input and output:
    - Input: 
        - A list of strings
        - N: number of mini lists that was broken from the master list.
    - Output: a list of N lists of strings.

##### Regular nStream
- Treat each mini list as a bucket to store the items.
- len(masterList)/N = n: the minimum number of strings will be in one bucket.
- If there's a remainder `len(masterList)%N = r`, r < N, the remaining items' position can be determined by just put the item one by one in each bucket, starting from bucket 0.
- Example: l = ["a","b","c","d","e"], N = 3
    - len(l)/N = 5/3 = 1, len(l)%N = 5%3 = 2 => each bucket has 1 element l0=["a"], l1=["b"], l2=["c"].
    - For "d" and "e" left, "d" is at position 3, 3%3=0, then add "d" to l0. "e" is at position 4, 4%3=1, then add "e" to l1.
    - Return [["a","d"],["b","e"],["c"]].
- Special cases: 
    - Empty master list => return N empty lists.
    - N is not a positive integer => raise exception!

##### Super mean twist nStream

### Pseudocode
1. If N is not postive integer => exception.
2. If master list is empty => return a list of N emptied lists.
3. Create a list of N lists
4. Calculate n (minimum items per each bucket) and r (the remainder)
    - Put n items in each buckets first.
    - Take the position of each element left, divided by N, get the remainder and that will be the position of the bucket.
5. Return the list of N lists.

### BigO