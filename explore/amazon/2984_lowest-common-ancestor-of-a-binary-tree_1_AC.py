# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
# post-order traverse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root, p, q):
            if root is None:
                return root, False, False

            lr, lfp, lfq = traverse(root.left, p, q)
            if lfp and lfq:
                return lr, lfp, lfq

            rr, rfp, rfq = traverse(root.right, p, q)
            if rfp and rfq:
                return rr, rfp, rfq

            fp = lfp or rfp or (root == p)
            fq = lfq or rfq or (root == q)

            # check if p and q are found within the subtree
            return root, fp, fq

        res, _, _ = traverse(root, p, q)
        return res
