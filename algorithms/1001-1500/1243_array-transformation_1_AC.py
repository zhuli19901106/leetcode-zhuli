# easy
# https://leetcode.com/problems/array-transformation/
# 1AC, brute force
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        a = arr
        n = len(a)
        while True:
            cnt = 0
            a1 = a[:]
            for i in range(1, n - 1):
                if a[i] < a[i - 1] and a[i] < a[i + 1]:
                    a1[i] += 1
                    cnt += 1
                    continue
                if a[i] > a[i - 1] and a[i] > a[i + 1]:
                    a1[i] -= 1
                    cnt += 1
                    continue
            a = a1
            if cnt == 0:
                break
        return a
