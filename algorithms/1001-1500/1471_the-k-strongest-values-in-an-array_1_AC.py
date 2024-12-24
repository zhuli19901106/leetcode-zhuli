# medium
# https://leetcode.com/problems/the-k-strongest-values-in-an-array/
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        if n == 0:
            return []

        med = arr[(n - 1) // 2]
        tups = []
        for x in arr:
            tups.append((-abs(x - med), -x))
        tups.sort()

        return [-x[1] for x in tups[:k]]
