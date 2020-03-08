# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# what's the point?
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            res = ['a' for i in range(n - 1)] + ['b']
        else:
            res = ['a' for i in range(n)]
        return ''.join(res)
