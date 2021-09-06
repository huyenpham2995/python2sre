# Function to find the largest palindrome substring in a string
# s: original string
# return largest palindrome substring
def largestPalindrome(s: str) -> str:
    # raising 2 exceptions for input is not a string
    if not isinstance(s, str):
        raise TypeError("Expecting string")

    # distant between left and right pointer
    dist = 0
    max_len = 0
    max_palindrome = ""
    
    # create the matrix nxn, where n is the length of the string
    # the rows represents position of left pointer, column for right
    t = [[0 for i in range(len(s))] for j in range(len(s))]

    for dist in range(0, len(s)):
        l = 0
        r = l + dist

        while r < len(s):
            # the substring only has 1 letter => it is a palindrome length 1
            if l == r:
                t[l][r] = 1
            else:
                # the 2 letters match
                if s[l] == s[r]:
                    # if the palindrome length is even (r pointer right next to left)
                    # eg: aa 
                    if l == r-1:
                        t[l][r] = t[l+1][r] + 1
                    # if the palindrome length is odd
                    # eg: aba
                    else:
                        t[l][r] = t[l+1][r-1] + 2
                # if the 2 letters don't match
                # current max palindrome will be max  between palindrome excluding s[l] ]
                # and max palindrome including s[r]
                else:
                    t[l][r] = max(t[l+1][r], t[l][r-1])
                
            # if current palindrome has length > max palindrome len
            if t[l][r] > max_len:
                max_len = t[l][r]
                max_palindrome = s[l:r+1]

            l = l+1
            r = r+1

    return max_palindrome