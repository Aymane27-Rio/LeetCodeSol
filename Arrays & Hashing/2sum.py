# Link: https://leetcode.com/problems/two-sum/description

# Given an array of integers nums and an integer target, return indices of 
# the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]


class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        sorted_nums = sorted(nums)
        i = 0
        j = n - 1
        if sorted_nums[i] + sorted_nums[j] == target:
            i = nums.index(sorted_nums[i])
            nums[i] = -1
            j = nums.index(sorted_nums[j])
            return [i, j]
        while sorted_nums[i] + sorted_nums[j] != target:
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
        i = nums.index(sorted_nums[i])
        nums[i] = -1
        j = nums.index(sorted_nums[j])
        return [i, j]