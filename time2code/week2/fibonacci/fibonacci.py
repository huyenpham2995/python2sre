# Input: n (int) - the position of the fibonacci number
# Output: the nth fibonacci number
def find_nth_fibonacci(n):
    # Invalid index
    if n < 1 or not isinstance(n, int):
        return None
    
    # base case: 1st fibonacci is 0, 2nd is 1
    if n == 1:
        return 0
    if n == 2:
        return 1

    # store all fibonacci numbers that have been found
    fib_arr = [0, 1]
    return find_nth_fibonacci_helper(n, fib_arr)


# Recursive function to find the nth fibonacci number
# Input: 
#       n (int) - the position of the fibonacci number
#       fib_arr (array of integers) - the array which stores the fibonacci #s that have been found
def find_nth_fibonacci_helper(n, fib_arr):
    if n <= len(fib_arr):
        return fib_arr[n-1]
    
    fib_n = find_nth_fibonacci_helper(n-1, fib_arr) + find_nth_fibonacci_helper(n-2, fib_arr)
    fib_arr.append(fib_n)

    return fib_n