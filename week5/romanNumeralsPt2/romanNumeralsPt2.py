romanNumeralsDict= {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}

def romanNumeralsPt2(s: str) -> int:
    # Empty string is invalid
    if len(s) == 0:
        return None
    
    # If there's only 1 letter, see if the letter is valid. 
    # If it is return the value
    s = s.upper()
    result = 0
    index = 0

    while index < len(s):
        # invalid if character does not exist in the dictionary
        if s[index] not in romanNumeralsDict.keys():
            return None

        # first one is auto added to the result
        if index == 0:
            result += romanNumeralsDict[s[index]]
        else:
            prevNum = romanNumeralsDict[s[index-1]]
            curNum = romanNumeralsDict[s[index]]
            if curNum < prevNum:
                result += curNum
            else:
                if curNum > result:
                    result = curNum - result
                else:
                    result -= prevNum
                    result += curNum - prevNum
        
        index += 1

    return result