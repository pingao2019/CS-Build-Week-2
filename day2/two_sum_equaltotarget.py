"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example: Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1]."""
# if sum of two elements in the lists = target,
#return a list that cotains indices of these two elements


def twoSum(nums, target ):
    dict={}
    for key,value  in enumerate(nums):
        if target -value in dict:
            return [dict[target-value], key]
        else:
            dict[value]=key
    return []
nums = [2, 7, 11, 15]
target = 9   
print(twoSum(nums, target))




