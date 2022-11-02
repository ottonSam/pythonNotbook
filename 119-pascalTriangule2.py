inputVar = 2

def pascalTriangle(rowIndex):
    if rowIndex == 0:
        return [1]
    
    newL = [1]
    oldL = pascalTriangle(rowIndex-1)
    for i in range(len(oldL) -1):
        newL.append(oldL[i] + oldL[i+1])
    newL.append(1)        
    return newL

print(pascalTriangle(inputVar))