inputVar = [2,3,1,1,4]

def canJump(nums):
    b = True
    it = nums[0]
    
    poss = nums[1:nums[0]+1]
        
    for i in range(len(poss)):
        if poss[i] > nums[0] - (i+1):
            it = i+1
            break
    
    if len(nums) > 2 and len(nums) > it:
        if nums[it] != 0:
            b = canJump(nums[it:])
            
    if b and 1 < len(nums) > it + 1:
        if nums[it] == 0:
            return False
    
    return b   

print(canJump(inputVar))