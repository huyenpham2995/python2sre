def validateParenthesis(string):
    if string == "":
        return True
    
    parenthesis = []

    # get all the parenthesis
    for char in string:
        if char == "(" or char == ")":
            parenthesis.append(char) 

    # Theres an odd number of parenthesis in this string
    # First parenthesis is a closing 
    if len(parenthesis) % 2 != 0 or parenthesis[0] == ")":
        return False  

    cur = 1
    while cur < len(parenthesis):
        if parenthesis[cur] == ")":
            # closing parenthesis is the 1st parenthesis encountered => false
            if cur == 0:
                return False
            # remove a pair of parenthesis if they are valid 
            # update index
            parenthesis.pop(cur)
            parenthesis.pop(cur - 1)
            cur = cur - 1
        else:
            cur += 1

    if len(parenthesis) > 0:
        return False

    return True