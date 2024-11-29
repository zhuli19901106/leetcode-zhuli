# https://leetcode.com/problems/separate-the-digits-in-an-array/
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digs = []
        res = []
        for x in nums:
            while x != 0:
                digs.append(x % 10)
                x //= 10
            while digs:
                res.append(digs.pop())
        return res
