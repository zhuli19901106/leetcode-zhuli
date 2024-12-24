# medium
# https://leetcode.com/problems/pancake-sorting/
# brute-force
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        a = A
        n = len(a)
        for i in range(n, 1, -1):
            mj = 0
            for j in range(1, i):
                if a[j] >= a[mj]:
                    mj = j
            if mj == i - 1:
                a.pop()
                continue
            if mj > 0:
                res.append(mj + 1)
            res.append(i)
            if i - 1 - mj > 1:
                res.append(i - 1 - mj)
            a = a[mj + 1:] + a[:mj + 1]
            a.pop()
        return res
