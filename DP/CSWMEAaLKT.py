# Count Subarrays Where Max Element Appears at Least K Times (CSWMEAaLKT)

# Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-09-25


#You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.


# Example 1:

# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: 
# [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].






# Brute force solution (so to speak)

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = max(nums)
        n = len(nums)
        if nums.count(m) < k:
            return 0
        subarrays = []
        for i in range(n):  
            for j in range(i, n):  
                subarray = nums[i : j + 1]
                if m in subarray and subarray.count(m) >= k:
                    subarrays.append(subarray)

        return len(subarrays)