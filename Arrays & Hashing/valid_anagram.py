# Link: https://leetcode.com/problems/valid-anagram/description

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(t)
        m = len(s)
        s_dict = {}
        t_dict = {}
        for char1 in s:
            s_dict[char1] = s_dict.get(char1, 0) + 1 # count characters in s
        for char2 in t:
            t_dict[char2] = t_dict.get(char2, 0) + 1 # count characters in t
            
        return s_dict == t_dict # compare the two dictionaries