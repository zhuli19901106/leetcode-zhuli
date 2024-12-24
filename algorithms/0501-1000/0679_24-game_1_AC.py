# hard
# https://leetcode.com/problems/24-game/
# pure brute-force search
from operator import add, sub, mul, truediv

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPS = 1e-6
        ops = [add, sub, mul, truediv]

        def dfs(a):
            if len(a) == 1:
                return abs(a[0] - 24) < EPS
            n = len(a)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    a1 = []
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        a1.append(a[k])
                    for op in ops:
                        if op == truediv and abs(a[j]) < EPS:
                            # zero division
                            continue
                        a1.append(op(a[i], a[j]))
                        ret = dfs(a1)
                        a1.pop()
                        if ret:
                            return True
            return False

        return dfs(nums)
