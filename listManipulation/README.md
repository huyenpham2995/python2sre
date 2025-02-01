### Question

You are given two lists, please do the following:
1) write a function named xor_lists to combine two lists with items in either list but not both.
example:
a = [1, 2, 3]
b = [2, 4, 6]
xor_lists(a, b) # [1, 3, 4, 6]
2) write a function named and_lists to combine two lists with items in both lists.
example:
a = [1, 2, 3]
b = [2, 4, 6]
and_lists(a, b) # [2]
3) write a function named left_lists to combine two lists with items from first list and not from second list
example:
a = [1, 2, 3]
b = [2, 4, 6]
left_lists(a, b) # [1, 3]

### BigO
- Xor: O(a+b)
- And: O(a+b)
- Left: O(a+b) (questionable because of the removing item part, which means it has to be searched.)