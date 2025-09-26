# Link: https://leetcode.com/problems/contains-duplicate/description


#Given an integer array nums, return true 
# if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.






# This solution may encounter a Time Limit Exceeded error for large inputs. 

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = []
        n = len(nums)
        for num in nums:
            if num in L:
                return True
            L.append(num)
        return False
    


# Optimal solution using a set 


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = set()
        n = len(nums)
        for num in nums:
            if num in L:
                return True
            L.add(num)
        return False