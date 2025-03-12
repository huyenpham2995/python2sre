ROMAN_NUMERAL_DICT= {1:"I", 4:"IV", 5:"V", 
                     9:"IX", 10:"X", 40:"XL", 
                     50:"L", 90:"XC", 100:"C", 500:"D", 1000:"M"}

def roman_numerals_pt3(num: int) -> str:
    if num < 1 or not isinstance(num, int):
        raise TypeError

    values = sorted(ROMAN_NUMERAL_DICT.keys())
    result = ""
    i=0

    while num > 0:
        i=0
        while i < len(values):
            if num < values[i]:
                break
            i+=1
        i -= 1
        num -= values[i]
        result += ROMAN_NUMERAL_DICT[values[i]]

    return result