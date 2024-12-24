# medium
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(root, arr):
            if root is None:
                return
            arr.append(root.val)
            traverse(root.left, arr)
            traverse(root.right, arr)

        a1 = []
        traverse(root1, a1)
        a2 = []
        traverse(root2, a2)
        a3 = a1 + a2
        res = sorted(a3)
        return res
