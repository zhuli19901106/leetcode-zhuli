# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# 1AC, count consecutive 0s and 1s
class Solution:
    def numSteps(self, s: str) -> int:
        if s == '' or s == '0':
            return -1

        a = list(s)[::-1]
        res = 0
        n = len(a)
        i = 0
        while i < n - 1:
            if a[i] == '0':
                i += 1
                res += 1
                continue
            j = 0
            while i < n and a[i] == '1':
                i += 1
                j += 1
            if i < n:
                a[i] = '1'
            else:
                a.append('1')
                n += 1
            res += j + 1
        return res
