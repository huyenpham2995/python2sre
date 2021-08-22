from collections import defaultdict
romanNumeralsDict = defaultdict(int)
romanNumeralsDict["I"] = 1
romanNumeralsDict["V"] = 5
romanNumeralsDict["X"] = 10
romanNumeralsDict["L"] = 50
romanNumeralsDict["C"] = 100
romanNumeralsDict["D"] = 500
romanNumeralsDict["M"] = 1000

def romanNumerals(string):
    # Empty string is invalid
    if len(string) == 0:
        return None
    
    # If there's only 1 letter, see if the letter is valid. 
    # If it is return the value
    result = 0
    cur = 0

    while cur < len(string):
        # invalid if character does not exist in the dictionary
        if romanNumeralsDict[string[cur].upper()] == 0:
            return None

        # first character will be added to the result sum automatically
        if cur == 0:
            result += romanNumeralsDict[string[cur].upper()]
        else:
            prevNum = romanNumeralsDict[string[cur-1].upper()]
            curNum = romanNumeralsDict[string[cur].upper()]
            if prevNum < curNum:
                result -= prevNum
                result += curNum - prevNum
            else:
                result += curNum 

        cur += 1    

    return result