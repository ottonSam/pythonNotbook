inputVar = ["bar", "rab", "aa", "", "avi", "iva"]

def groupAnagrams(strs):
    anagrams = {}
    result = []
    for str in strs:
        key = ''.join(sorted(str))
        if anagrams.get(key):
            anagrams[key].append(str)
        else:
            anagrams[key]=[str]
    for a in anagrams:
        result.append(anagrams[a])
    return result
print(groupAnagrams(inputVar))