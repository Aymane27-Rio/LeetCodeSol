# Link:  https://leetcode.com/problems/reverse-integer/description/


# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
# value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        x1 = abs(x)
        y = str(x1)[::-1]
        res = int(y) if x >= 0 else -int(y)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
