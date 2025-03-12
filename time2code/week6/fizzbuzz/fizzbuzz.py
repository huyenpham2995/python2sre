def fizzbuzz(num: float):
    result = ""

    try:
        num = float(num)
        if num % 3 != 0 and num % 5 != 0:
            return num
        else:
            if num % 3 == 0:
                result = "fizz"
            if num % 5 == 0:
                result += "buzz"
    except Exception:
        raise ValueError("Expected a number")
        
    return result