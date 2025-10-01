# Link: https://leetcode.com/problems/search-a-2d-matrix/description



# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.






# This solution passes 107/133 test cases

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            return target in matrix[i]
        return False



# This solution passes 133/133 test cases

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            left = 0 
            right = len(matrix[i]) - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[i][middle] == target:
                    return True
                elif matrix[i][middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        return False