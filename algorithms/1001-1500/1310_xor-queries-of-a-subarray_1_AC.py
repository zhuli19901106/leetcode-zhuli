# medium
# https://leetcode.com/problems/xor-queries-of-a-subarray/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        apx = [0 for i in range(n + 1)]
        for i in range(n):
            apx[i + 1] = apx[i] ^ arr[i]
        res = []
        for i1, i2 in queries:
            res.append(apx[i2 + 1] ^ apx[i1])
        return res
