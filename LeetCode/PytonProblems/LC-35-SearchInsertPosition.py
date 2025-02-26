# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0

        if nums[-1] < target:
            return (len(nums))
        elif nums[0] > target:
            return 0

        while (nums[i] <= target):
            if (nums[i] == target):
                return i
            elif (nums[i+1] > target):
                return i + 1
            i += 1