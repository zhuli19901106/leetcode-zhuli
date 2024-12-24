# medium
# https://leetcode.com/problems/implement-rand10-using-rand7/
# simple probability problem
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            x = rand7() - 1
            y = rand7() - 1
            z = x * 7 + y
            if z < 40:
                break
        return z // 4 + 1
