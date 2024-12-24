# medium
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# 1AC, level order traversal
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        q = deque()
        u_dep = None
        q.append((root, 0))
        while len(q) > 0:
            node, dep = q.popleft()
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))

            if u_dep is None:
                if node is u:
                    u_dep = dep
            elif dep == u_dep:
                return node
            else:
                break
        return None
