romanNumeralsDict= {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}

def romanNumeralsPt2(string):
    # Empty string is invalid
    if len(string) == 0:
        return None
    
    # If there's only 1 letter, see if the letter is valid. 
    # If it is return the value
    string = string.upper()
    result = 0
    index = 0

    while index < len(string):
        # invalid if character does not exist in the dictionary
        if string[index] not in romanNumeralsDict.keys():
            return None

        # first character will be added to the result sum automatically
        if index == 0:
            result += romanNumeralsDict[string[index]]
        else:
            prevNum = romanNumeralsDict[string[index-1]]
            curNum = romanNumeralsDict[string[index]]
            if prevNum < curNum:
                result -= prevNum
                result += curNum - prevNum
            else:
                result += curNum 

        index += 1    

    return result