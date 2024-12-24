# medium
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(r1, r2, dep):
            if r1 is None or r2 is None:
                return
            if dep % 2 == 1:
                v1, v2 = r1.val, r2.val
                r1.val, r2.val = v2, v1
            traverse(r1.left, r2.right, dep + 1)
            if r1 != r2:
                traverse(r1.right, r2.left, dep + 1)

        traverse(root, root, 0)

        return root
