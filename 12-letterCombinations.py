inputVar = "5235634783672"

def letterCombinations(digits):
    dici = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    typeds = []
    
    if len(digits) == 0:
        return([])
    
    if len(digits) > 1:
        typeds = letterCombinations(digits[1:])
    elif len(digits) == 1:
        return dici[digits[0]]
    
    nTypeds = []
    for i in dici[digits[0]]:
        for j in typeds:
            nTypeds.append(i+j)
    
    return(nTypeds)

print(letterCombinations(inputVar))