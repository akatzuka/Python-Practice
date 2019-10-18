import numpy as np  #Unused

def twoSum(nums, target):
  i_map = {}
  for i in range(len(nums)):
    num = nums[i]
    remain = target - num
    if remain in i_map:
      return[i_map[remain], i]
    i_map[num] = i
  return None

nums = [10, 2, 7, 30, 52]   #example list/array
target = 9

print("Nums: ", nums)
print("Target: ", target)
print("Solution: ", twoSum(nums, target))
