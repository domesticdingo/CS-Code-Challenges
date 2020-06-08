#Given an array of int, return indices of the two numbers such that they add up to a specific target
#Assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}

        for i, num in enumerate(nums):
            if target - num in hash_table.keys():
                return [hash_table[target - num], i]
            hash_table[num] = i
        return None