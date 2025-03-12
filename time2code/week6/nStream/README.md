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
- minItems = len(masterList)/N = n: the minimum number of strings will be in one bucket.
- If there's a remainder `len(masterList)%N = r`, r < N, the remaining items' position can be determined by just put the item one by one in each bucket, starting from bucket 0.
- Example: l = ["a","b","c","d","e"], N = 3
    - minItems = len(l)/N = 5/3 = 1, len(l)%N = 5%3 = 2 => each bucket has 1 element l0=["a"], l1=["b"], l2=["c"].
    - For "d" and "e" left, "d" is at position 3, 3%3=0, then add "d" to l0. "e" is at position 4, 4%3=1, then add "e" to l1.
    - Return [["a","d"],["b","e"],["c"]].
- Special cases: 
    - Empty master list => return N empty lists.
    - N is not a positive integer => raise exception!

##### Super mean twist nStream
- Can't keep count of output array size and can't use the size of the list. The only thing we can do to determine the position of each item is based on its index => hashing!
- Can use the modulo equation to find the correct bucket for each item.
- Example: ["a","b","c","d","e"], N = 3
    - "a" is at position 0. 0%3=0, "a" goes to bucket 0
    - "b" is at position 1. 1%3=1, "b" goes to bucket 1
    - "c" is at position 2. 2%3=2, "c" goes to bucket 2
    - "d" is at position 3. 3%3=0, "d" goes to bucket 0
    - "e" is at position 4. 4%3=1, "e" goes to bucket 1

### Pseudocode
##### Regular nStream
1. If N is not postive integer => exception.
2. If master list is empty => return a list of N emptied lists.
3. Create a list of N lists
4. Calculate n (minimum items per each bucket) and r (the remainder)
    - Put n items in each buckets first.
    - Take the position of each element left, divided by N, get the remainder and that will be the position of the bucket.
5. Return the list of N lists.

##### Super mean twist nStream
1. If N is not postive integer => exception.
2. Create result list which contains N empty lists
3. Go through each item in the master list one by one and determine their position based on their position.
4. Return result

### BigO
- In the worst case scenerio (N=1), go through every elements in the master list => time complexity O(n) (n is the length of the master list). 
- In the worst case scenerio (N=1), created n buckets which are contain in the result list => O(n) (n is the length of the master list). 