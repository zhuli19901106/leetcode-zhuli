# medium
# https://leetcode.com/problems/global-and-local-inversions/
# after second thought, it's supposed to be quite easy
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        a = A
        n = len(a)
        i = 0
        while i < n - 1:
            if a[i] < a[i + 1]:
                i += 1
            else:
                a[i], a[i + 1] = a[i + 1], a[i]
                i += 2
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                return False
        return True
'''
# TLE, although counting inversion can be done by tweaking merge sort, I'll go with BIT
class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0 for i in range(n + 1)]

    def sum(self, idx):
        a = self.a
        n = self.n
        if idx < 1:
            return 0
        idx = min(idx, n)
        res = 0
        while idx >= 1:
            res += a[idx]
            idx -= (idx & -idx)
        return res

    def add(self, idx, val):
        a = self.a
        n = self.n
        if idx < 1 or idx > n:
            return
        while idx <= n:
            a[idx] += val
            idx += (idx & -idx)

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        a = A
        n = len(a)

        # count local inversion
        loc = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                loc += 1

        # count global inversion
        bit = BIT(n)
        glo = 0
        for i, x in enumerate(a):
            glo += i - bit.sum(x + 1)
            bit.add(x + 1, 1)
        return loc == glo
'''