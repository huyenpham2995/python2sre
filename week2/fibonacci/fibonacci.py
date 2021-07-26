# Input: n (int) - the position of the fibonacci number
# Output: the nth fibonacci number
def findNthFibonacci(n):
    # Invalid index
    if n < 1 or not isinstance(n, int):
        return None
    
    # base case: 1st fibonacci is 0, 2nd is 1
    if n == 1:
        return 0
    if n == 2:
        return 1

    # store all fibonacci numbers that have been found
    fibArr = [0, 1]
    return findNthFibonacciHelper(n, fibArr)


# Recursive function to find the nth fibonacci number
# Input: 
#       n (int) - the position of the fibonacci number
#       fib_arr (array of integers) - the array which stores the fibonacci #s that have been found
def findNthFibonacciHelper(n, fibArr):
    if n <= len(fibArr):
        return fibArr[n-1]
    
    fibN = findNthFibonacciHelper(n-1, fibArr) + findNthFibonacciHelper(n-2, fibArr)
    fibArr.append(fibN)

    return fibN