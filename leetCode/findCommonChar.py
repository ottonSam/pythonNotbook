inputVar = ["bella","labe","roller"]

def findCommonChar(words):
    repeat = list(words[0])
    for word in words:
        list(word)
        nRepeat = []
        for w in word:
            if w in repeat:
                nRepeat.append(w)
                repeat.remove(w)
        repeat = nRepeat
    return repeat