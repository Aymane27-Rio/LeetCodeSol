# Link: https://leetcode.com/problems/search-insert-position/description/


# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        stop = target
        if stop < min(nums):
            return 0
        if stop > max(nums):
            return len(nums)
        while stop not in nums:
            stop -= 1
        return nums.index(stop) + 1