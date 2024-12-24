# medium
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class NodeInfo:
    def __init__(self, min_val, max_val, max_diff):
        self.min_val = min_val
        self.max_val = max_val
        self.max_diff = max_diff

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def traverse(root):
            if root is None:
                return None
            
            max_diff = 0
            min_val = max_val = root.val

            if not root.left is None:
                nl = traverse(root.left)
                min_val = min(min_val, nl.min_val)
                max_val = max(max_val, nl.max_val)
                max_diff = max(max_diff, nl.max_diff)

            if not root.right is None:
                nr = traverse(root.right)
                min_val = min(min_val, nr.min_val)
                max_val = max(max_val, nr.max_val)
                max_diff = max(max_diff, nr.max_diff)

            max_diff = max(max_diff, abs(root.val - min_val), abs(root.val - max_val))
            return NodeInfo(min_val, max_val, max_diff)

        node = traverse(root)
        return node.max_diff
