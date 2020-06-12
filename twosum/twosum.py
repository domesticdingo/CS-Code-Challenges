class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}

        for i, num in enumerate(nums):
            if target - num in hash_table.keys():
                return [hash_table[target - num], i]
            hash_table[num] = i
        return None