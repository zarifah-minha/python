def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        print ("List of the items having the same first and last characters", lst)
        return ctr

count= match_words(["xyz", "abc", "wow", "codingal", "1221"])
print("Total count of the items having the same first and last characterP:", count)