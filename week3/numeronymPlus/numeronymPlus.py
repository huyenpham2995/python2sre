def verifyNumeronymPlus(numeronym, word):
    # both "" or one of the input is ""
    if numeronym == "":
        # if both are "" => True
        if word == "":
            return True
        # if word is not "" => False
        else: 
            return False
    else:
        # if numeronym is not "" but word is "" => False
        if word == "":
            return False

    # Both are not ""
    # if first or (and) last character of numeronym is not a letter
    if not numeronym[0].isalpha() or not numeronym[-1].isalpha():
        return False

    return False