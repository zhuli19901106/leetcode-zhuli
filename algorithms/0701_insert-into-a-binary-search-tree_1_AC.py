# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        ptr = root
        while True:
            if val < ptr.val:
                if not ptr.left is None:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(val)
                    break
            elif val > ptr.val:
                if not ptr.right is None:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(val)
                    break
            else:
                break
        return root
