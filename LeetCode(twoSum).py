'''Issue: return indices of the two numbers such that they add up to target.'''

def twoSum(nums, target):
    answer = {}
    for i, value in enumerate(nums):
        if (target - value) in answer:
            return (answer[target - value], i)
        else:
            answer[value] = i
print(twoSum([3, 4, 2], 6))
