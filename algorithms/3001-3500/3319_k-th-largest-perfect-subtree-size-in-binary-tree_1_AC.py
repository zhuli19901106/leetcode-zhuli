# medium
# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        res = []
        self.traverse(root, res)

        res.sort(reverse=True)
        return res[k - 1] if len(res) >= k else -1

    def traverse(self, root, res):
        if root.left is None and root.right is None:
            res.append(1)
            return 1

        ln = -1
        if root.left:
            ln = self.traverse(root.left, res)

        rn = -1
        if root.right:
            rn = self.traverse(root.right, res)

        if ln > 0 and rn > 0 and ln == rn:
            total = ln + rn + 1
            res.append(total)
            return total

        return -1
