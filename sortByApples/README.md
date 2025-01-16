### Question
You are given a CSV file with following content:
```
apple,banana,orange,grape,grapefruit
apple,pineapple,orange,grape,apple
orange,banana,orange,grape,cherry,pineapple
apple,peach,durian,grape,apple,apple,banana,kiwi
apple,grape,orange,apple,pineapple,apple
```
Please sort all the lines by the percentage of 'apple' occurs per line from largest to smallest, then save it to a new file.

### Thoughts
- The fastest way to find a line based on a key is by using dictionary. In this case, the key will be the % of apple in the line, and the value will be an array with each line being an element.
- Why array? There exists a situation where the % of apple between 2 lines are the same.
- How to count the amount of apples in 1 line?
   - Loop through all word in line and count. If line has K word, this is O(K) operations -> this way is faster generally.
   - Sort the line. 'apple' will be next to each other so once there' a different word, break. O(KlogK)

### Pseudocode
- Open file and check for error. Create a dictionary called fruits to store the lines.
- For each line in the file
   - Use regex to find the number of the word 'apple'
   - Split line by comma and count length
   - Caculate the % of'apple' by num_of_apple/line length (keep it as float)
   - Insert it in the dictionary with the key being the %, value is the line itself.
- Sort dictionary by key
- Print.

### BigO
- Go through each line of the file -> O(N)
- If each line has K words, find $ of 'apple' takes O(K). In total O(NK) for the whole file.
- Sort the dictionary by key O(NlogN).
- Print O(N)

-> In general, it depends on how big is N and K. Imagine by standard, a line should not be < 80 characters, then K is a constant. N can go infinitely. With this assumption, O(NK) becomes O(N), then the biggest number here will be O(NlogN) -> O(NlogN).