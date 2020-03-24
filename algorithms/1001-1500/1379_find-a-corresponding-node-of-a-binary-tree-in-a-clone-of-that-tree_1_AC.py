# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# 1AC, straightforward
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if target is None:
            return None

        def traverse(r1, r2):
            if r1 is target:
                return r2
            if r1.left:
                res = traverse(r1.left, r2.left)
                if res:
                    return res
            if r1.right:
                res = traverse(r1.right, r2.right)
                if res:
                    return res
            return None

        return traverse(original, cloned)
