# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a1 = list(map(sum, mat))
        a2 = list(enumerate(a1))
        a2.sort(key=lambda x: x[1])
        a3 = list(map(lambda x: x[0], a2))
        return a3[:k]
