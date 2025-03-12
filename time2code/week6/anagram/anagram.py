from collections import defaultdict

def verifyAnagram(word1: str, word2: str) -> bool:
    # if 2 words have different length
    if len(word1) != len(word2):
        return False

    word1_dict = defaultdict(int)
    word2_dict = defaultdict(int)

    # create 2 dictionaries out of 2 words
    for i in range(len(word1)):
        word1_dict[word1[i]] += 1
        word2_dict[word2[i]] += 1

    # Compare each entry in the dictionaries
    for char in word1_dict.keys():
        if word1_dict[char] != word2_dict[char]:
            return False

    return True