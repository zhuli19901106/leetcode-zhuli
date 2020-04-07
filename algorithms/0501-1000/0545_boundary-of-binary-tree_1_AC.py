# https://leetcode.com/problems/boundary-of-binary-tree/
# https://leetcode.com/problems/boundary-of-binary-tree/discuss/563845/Python-DFS
# my implementation was much longer and trickier, I gave up
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []

        def traverse(root, lm, rm):
            nonlocal res

            if root is None:
                return
            if lm:
                res.append(root.val)
            if (root.left is None and root.right is None) and\
                (not lm and not rm):
                res.append(root.val)
            traverse(root.left, lm, rm and (root.right is None))
            traverse(root.right, lm and (root.left is None), rm)
            if rm:
                res.append(root.val)

        res.append(root.val)
        traverse(root.left, True, False)
        traverse(root.right, False, True)
        return res
