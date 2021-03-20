# https://leetcode.com/problems/check-array-formation-through-concatenation/
# 1AC, brute force DFS
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        vs = [False for _ in range(len(pieces))]
        return self.dfs(arr, 0, pieces, vs)

    def dfs(self, arr, idx, pieces, vs):
        if idx == len(arr):
            return True
        for i in range(len(vs)):
            if vs[i]:
                continue
            j = 0
            m = len(pieces[i])
            while j < m:
                if arr[idx + j] != pieces[i][j]:
                    break
                j += 1
            if j < m:
                continue
            vs[i] = True
            ret = self.dfs(arr, idx + m, pieces, vs)
            if ret:
                return True
            vs[i] = False
        return False
