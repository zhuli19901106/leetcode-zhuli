# https://leetcode.c1om/problems/reduce-array-size-to-the-half/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = {}
        for x in arr:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        ac = list(m.items())
        ac.sort(reverse=True, key=lambda x: x[1])
        n = len(arr)
        m = 0
        res = 0
        for x in ac:
            if m >= (n + 1) // 2:
                break
            m += x[1]
            res += 1
        return res
