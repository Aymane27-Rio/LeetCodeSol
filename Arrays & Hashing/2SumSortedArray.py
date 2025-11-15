# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that 
# they add up to a given target number target and index1 < index2. Note that 
# index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use O(1) additional space.






class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
        while i != j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return[i + 1, j + 1]