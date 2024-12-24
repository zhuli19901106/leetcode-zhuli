# easy
# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/
# 1AC, sort and count
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        a = arr
        a.sort()
        val = 5000
        res = 0
        for x in a:
            if val < x:
                break
            val -= x
            res += 1
        return res
