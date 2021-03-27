# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# 1AC, cumulative sum

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        a1 = [0 for _ in range(n)]
        cc, cur = 0, 0
        for i in range(n):
            a1[i] = cur
            if boxes[i] == '1':
                cc += 1
            cur += cc

        a2 = [0 for _ in range(n)]
        cc, cur = 0, 0
        for i in range(n - 1, -1, -1):
            a2[i] = cur
            if boxes[i] == '1':
                cc += 1
            cur += cc

        res = [0 for i in range(n)]
        for i in range(n):
            res[i] = a1[i] + a2[i]
        return res
