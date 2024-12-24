# medium
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# That's boring, man.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def traverse(par, root, m):
            if root is None:
                return None
            if not par is None:
                m[root] = par
            traverse(root, root.left, m)
            traverse(root, root.right, m)

        m = {}
        traverse(None, root, m)
        res = 0
        for ptr, par1 in m.items():
            if not par1 in m:
                continue
            par2 = m[par1]
            if par2.val % 2 == 0:
                res += ptr.val
        return res
