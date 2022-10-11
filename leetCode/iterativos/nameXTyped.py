name = "alex"
typed = "aleeex"

def isLongPressedName(name, typed):
    nName = []
    nTyped = []
    
    for i in name:
        if len(nName)>0:
            if i == nName[-1][0]:
                nName[-1][1] += 1
            else: 
                nName.append([i, 1])
        else: 
            nName.append([i, 1])
            
    for i in typed:
        if len(nTyped)>0: 
            if i == nTyped[-1][0]:
                nTyped[-1][1] += 1
            else:
                nTyped.append([i, 1])
        else:
            nTyped.append([i, 1])
    
    if len(nName) != len(nTyped):
        return False
    
    for i in range(len(nName)):
        if nName[i][0] != nTyped[i][0] or nName[i][1] > nTyped[i][1]:
            return False
    
    return True

print(isLongPressedName(name, typed))