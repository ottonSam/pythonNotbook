inputVar = [1, 2, 2, 2]

def singleNum(nums):
    return (int) ((sum(list(set(nums)))*3 - sum(nums))/2)

print(singleNum(inputVar))