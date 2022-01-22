# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(self, nums: List[int], target: int) -> List[int]:
  d = {};
  for i, num in enumerate(nums):
    if target-num not in d.keys():
      d[num] = i
    else:
      return d[target-num], i
