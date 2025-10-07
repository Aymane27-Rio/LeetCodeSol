# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].




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
        