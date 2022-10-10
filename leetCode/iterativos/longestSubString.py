inputVar = " "

def longestSubString(s):
    longestSub = 0

    if len(s) > 0:
        longestSub = 1

    for i in range(len(s)):
        subString = s[i]

        for j in range(i + 1, len(s)):
            if s[j] in subString:
                break
            
            subString += s[j]
            
            if len(subString) > longestSub:
                longestSub = len(subString)

    return longestSub

print(longestSubString(inputVar))