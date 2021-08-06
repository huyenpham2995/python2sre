def verifyNumeronym(numeronym, word):
    # if word is ""
    if word == "":
        return False

    # checking the length of the middle part of word, if first and last character are matching
    if numeronym[0] == word[0] and numeronym[-1] == word[-1]:
        expectedWordLength = int(numeronym[1:-1])
        if len(word[1:-1]) == expectedWordLength:
            return True
    
    #if first and last character do not match
    return False