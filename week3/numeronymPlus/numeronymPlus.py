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

    i = 0 # current position of numeronym
    j = 0 # current position of word

    # traverse through each character of numeronym
    while i < len(numeronym):
        expectedLength = 1
        currNumeronymChar = numeronym[i]
        
        # if the character is the letter, compare to the current letter of word
        if currNumeronymChar.isalpha():
            if currNumeronymChar != word[i]:
                return False

        # if the character is a number, grab all the numbers
        elif currNumeronymChar.isnumeric():
            #get the expected length
            expectedLength = ""
            while currNumeronymChar.isnumeric():
                expectedLength += currNumeronymChar
                i += 1
                currNumeronymChar = numeronym[i]
            i -= 1
            expectedLength = int(expectedLength)

            # if the expected length > the length of word from position i to the end => False
            if expectedLength > len(currNumeronymChar[j:]):
                return False
        
        i += 1
        j += expectedLength 

    # word is longer than numeronym
    if j < len(word) - 1:
        return False

    return True