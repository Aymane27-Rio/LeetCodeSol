# Link: https://leetcode.com/problems/powx-n/description/


# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25



# Still working on it


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            if n > 0:
                return 0
            return None
        
        negative = n < 0
        exp = -n if negative else n

        result = 1.0
        base = float(x)

        # binary exponentiation
        while exp:
            if exp & 1:
                result *= base
            base *= base
            exp >>= 1

        return 1.0 / result if negative else result
        if n >= 0:
            for i in range(n):
                result *= x
        else:
            for i in range(-n):
                result *= 1/x
        return result