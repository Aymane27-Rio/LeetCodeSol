# Link: https://leetcode.com/problems/longest-palindromic-substring/description/



# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def search(left, right):
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        result = ""
        n = len(s)
        for i in range(n):
            sub1 = search(i, i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = search(i, i + 1)
            if len(sub2) > len(result):
                result = sub2
        return result