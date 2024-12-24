# medium
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# post order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        INT_MIN = -(2 ** 31)

        def traverse(root, sum_val):
            res = INT_MIN
            if not root.left is None:
                ln, ls = traverse(root.left, sum_val + root.left.val)
                root.left = ln
                res = max(res, ls)
            if not root.right is None:
                rn, rs = traverse(root.right, sum_val + root.right.val)
                root.right = rn
                res = max(res, rs)
            if res == INT_MIN:
                res = sum_val
            if res < limit:
                return None, res
            return root, res

        if root is None:
            return root
        root, res = traverse(root, root.val)
        return root
