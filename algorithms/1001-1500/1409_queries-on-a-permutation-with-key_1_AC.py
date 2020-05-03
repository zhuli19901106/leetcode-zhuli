# https://leetcode.com/problems/queries-on-a-permutation-with-key/
# 1AC, just brute-force
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a = list(range(1, m + 1))
        res = []
        for q in queries:
            i = a.index(q)
            res.append(i)
            del a[i]
            a.insert(0, q)
        return res
