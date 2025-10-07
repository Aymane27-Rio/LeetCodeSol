# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/







class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            first = nums.index(target)
            last = len(nums) - 1 - nums[::-1].index(target)
            return [first, last]
        return [-1, -1]
        return [-1, -1]
        