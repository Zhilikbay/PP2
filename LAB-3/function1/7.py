def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

x=has_33([1, 3, 3]) 
y=has_33([1, 3, 1, 3])
z=has_33([3, 1, 3])
print(x,y,z)
