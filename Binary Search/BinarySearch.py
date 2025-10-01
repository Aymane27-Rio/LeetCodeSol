# Link: https://leetcode.com/problems/binary-search/description

# Given an array of integers nums which is sorted in ascending order, and an integer target,
#  write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1