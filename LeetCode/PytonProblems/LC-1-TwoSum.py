# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        length = len(nums)

        for i in range(length):
            complement = target - nums[i]
            if complement in numMap:
                return[i, numMap[complement]]
            numMap[nums[i]] = i