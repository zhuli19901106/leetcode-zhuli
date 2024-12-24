# medium
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# post order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class NodeInfo:
    def __init__(self, node, num, depth):
        self.node = node
        self.num = num
        self.depth = depth

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def traverse(root, depth):
            if root is None:
                return NodeInfo(root, 0, depth)
            left_info = traverse(root.left, depth + 1)
            right_info = traverse(root.right, depth + 1)

            info = NodeInfo(root, 1, depth)
            if left_info.num > 0:
                info = left_info
            if right_info.num > 0:
                if right_info.depth > info.depth:
                    info = right_info
                elif right_info.depth == info.depth:
                    info = NodeInfo(root, info.num + right_info.num, info.depth)
            return info

        node_info = traverse(root, 1)
        return node_info.node
