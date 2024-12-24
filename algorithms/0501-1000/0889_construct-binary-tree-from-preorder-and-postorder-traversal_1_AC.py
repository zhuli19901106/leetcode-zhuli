# medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Runtime: 48 ms, faster than 86.86% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pre_indices = {}
        post_indices = {}
        for i, x in enumerate(pre):
            pre_indices[x] = i
        for i, x in enumerate(post):
            post_indices[x] = i

        def traverse(pre, post, x1, y1, x2, y2):
            if x1 == y1:
                return TreeNode(pre[x1])
            root = TreeNode(pre[x1])
            xx1 = x1 + 1
            xx2 = x2
            yy2 = post_indices[pre[xx1]]
            yy1 = xx1 + (yy2 - xx2)
            root.left = traverse(pre, post, xx1, yy1, xx2, yy2)
            if yy2 + 1 == y2:
                return root

            root.right = traverse(pre, post, yy1 + 1, y1, yy2 + 1, y2 - 1)
            return root

        n = len(pre)
        return traverse(pre, post, 0, n - 1, 0, n - 1)
