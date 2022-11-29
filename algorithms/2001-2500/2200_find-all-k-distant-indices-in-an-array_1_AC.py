# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ai = []
        for i, x in enumerate(nums):
            if x == key:
                ai.append(i)
        
        res = []
        n, m = len(nums), len(ai)
        j = 0
        for i in range(n):
            while j < m and i > ai[j] + k:
                j += 1
            if j >= m:
                break
            
            if i >= ai[j] - k:
                res.append(i)

        return res
