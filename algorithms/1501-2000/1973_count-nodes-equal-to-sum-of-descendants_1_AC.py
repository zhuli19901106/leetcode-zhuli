# medium
# https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/
# 1AC, recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        _, res = self.getNodeSum(root)

        return res

    def getNodeSum(self, root):
        if root is None:
            return 0, 0

        left_sum, left_cnt = self.getNodeSum(root.left)
        right_sum, right_cnt = self.getNodeSum(root.right)
        cur = 1 if left_sum + right_sum == root.val else 0

        return root.val + left_sum + right_sum, cur + left_cnt + right_cnt
