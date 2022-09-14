inputVar = [3,1,1]
def hIndex(citations):
    hi = 0
    i = 0
    for c in sorted(citations):
        j = 0
        while(True):
            if j < len(citations)-i and j < c:
                j += 1
            else:
                if j > hi:
                    hi = j
                break
        i+=1
    return hi
print(hIndex(inputVar))