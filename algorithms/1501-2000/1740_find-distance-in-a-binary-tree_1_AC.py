# medium
# https://leetcode.com/problems/find-distance-in-a-binary-tree/
# careful with edge cases

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        cp, cq = self.traverse(root, p, q)
        return cp + cq

    def traverse(self, root, p, q, ):
        if root is None:
            return -1, -1

        cp, cq = -1, -1
        if root.val == p:
            cp = 0
        if root.val == q:
            cq = 0

        lp, lq = self.traverse(root.left, p, q)
        if lp != -1 and lq != -1:
            return lp, lq
        rp, rq = self.traverse(root.right, p, q)
        if rp != -1 and rq != -1:
            return rp, rq

        if cp == -1:
            cp = lp + 1 if lp != -1 else rp + 1 if rp != -1 else -1
        if cq == -1:
            cq = lq + 1 if lq != -1 else rq + 1 if rq != -1 else -1
        return cp, cq
