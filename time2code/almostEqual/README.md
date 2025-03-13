# Question

Given two strings, check if they are almost equal

Definition of almost equal:
For any string a and string b, a is one character different from b.

- True:
xyz, xyc
xyz, xy
xyz, xz
xyz, yz
xyz, xyzz
xyz, xayz
x, ''

- False:
xyz, xyz
xyz, xzy
xyz, xk
xyz, yzxt

# Thoughts
- The 2 words can have the same length or one word just has 1 character longer than the other.
- If there are more than 1 characters different between the 2 words -> False
- If there are 0 character difference
   - In this case, the length has to be different to make the 1 difference between them (eg: xyz and xyzz, both have x,y,z but there's an extra z)
- If there's 1 chacter difference: they can be either the same length, or 1 character apart from each other

# BigO
- Time: what matters here is how much time to calculate the difference. Let say the length of word1 is N and word2 is M (N>M). When word1 and word2 is converted into sets, the most characters it can have in the set is 26, so O(1). Calculating the difference between the sets requires going through all characters in set of word1 O(1), then see if it has in word2, also maximum O(1)