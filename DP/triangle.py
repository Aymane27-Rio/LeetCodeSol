# Link: https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25



# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. 
# More formally, if you are on index i on the current row, 
# you may move to either index i or index i + 1 on the next row.

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for k in range(len(triangle[i])):
                triangle[i][k] = triangle[i][k] + min(triangle[i+1][k], triangle[i+1][k+1])
        return triangle[0][0]