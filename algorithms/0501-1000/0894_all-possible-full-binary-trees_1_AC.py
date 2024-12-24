# medium
# https://leetcode.com/problems/all-possible-full-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if  N % 2 == 0:
            return []
        def possibleTree(n, res):
            if n in res:
                return res[n]
            arr =  []
            for i in range(1, n - 1, 2):
                atl = possibleTree(i, res)
                atr = possibleTree(n - 1 - i, res)
                for tl in atl:
                    for tr in atr:
                        r = TreeNode(0)
                        r.left = tl
                        r.right = tr
                        arr.append(r)
            res[n] = arr
            return arr
        res = {}
        res[1] = [TreeNode(0)]
        return possibleTree(N, res)
