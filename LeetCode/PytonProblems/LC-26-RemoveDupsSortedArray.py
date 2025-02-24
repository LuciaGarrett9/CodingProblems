# Given an integer array nums sorted in non-decreasing order
# remove the duplicates in-place such that each unique element appears only once
# The relative order of the elements should be kept the same
# Then return the number of unique elements in nums

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1

        length = len(nums)

        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k