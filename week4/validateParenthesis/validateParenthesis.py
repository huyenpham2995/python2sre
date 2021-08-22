def validateParenthesis(string):
    if string == "":
        return True
    
    prev = -1
    curr = 0
    parenthesis = []

    for char in string:
        if char == "(" or char == ")":
            parenthesis.append(char)

    return ""