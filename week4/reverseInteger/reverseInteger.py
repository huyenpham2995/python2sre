def reverseInteger(num):
    if num == "":
        return num
    
    # a flag to see if string has comma(s)
    hasComma = False
    reversedNum = ""

    # travese the string in reverse order
    for char in num[::-1]:
        if char == ",":
            hasComma = True
        else:
            reversedNum += char
    
    # convert it into an int to eliminate the 0(s), then back to string
    reversedNum = str(int(reversedNum))

    # add back the comma(s)
    if hasComma and len(reversedNum) > 3:
        commaPos = len(reversedNum) - 3

        while commaPos > 0:
            reversedNum = reversedNum[:commaPos] + "," + reversedNum[commaPos:]
            commaPos -= 3

    return reversedNum
