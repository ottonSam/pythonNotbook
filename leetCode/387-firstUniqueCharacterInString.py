inputVar = "aabb"
def firstUniqueChar(s):
    nr = {}
    r = {}
    l = []
    for i in range(len(s)):
        if s[i] in nr:
            if(s[i] in r):
                r.pop(s[i])
        else:
            nr[s[i]] = True
            r[s[i]] = i
            
    for i in r:
        l.append(r[i])
    if len(l) > 0:
        return(sorted(l)[0])
    return -1
print(firstUniqueChar(inputVar))