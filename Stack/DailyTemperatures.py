# Link: https://leetcode.com/problems/daily-temperatures/description/



# Given an array of integers temperatures represents the daily temperatures, return an array answer such that
#  answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]




#Brute force and gives time limit exceeded in some cases

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = []
        n = len(temperatures)
        for i in range(n):
            l = 0
            # if i == n-1:
            #     answer.append(0)
            #     return answer
            for k in range(i + 1, n):
                l += 1
                if temperatures[k] > temperatures[i]:
                    answer.append(l)
                    break
            else:
                answer.append(0)
        return answer



# Much better solution with complexity O(n)


class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer