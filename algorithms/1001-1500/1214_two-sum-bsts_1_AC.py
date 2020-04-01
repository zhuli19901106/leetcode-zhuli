# https://leetcode.com/problems/two-sum-bsts/
# 1AC, no surprise
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def traverse1(root, st):
            if root is None:
                return
            st.add(root.val)
            traverse1(root.left, st)
            traverse1(root.right, st)

        def traverse2(root, st, target):
            if root is None:
                return False
            if target - root.val in st:
                return True
            if traverse2(root.left, st, target):
                return True
            if traverse2(root.right, st, target):
                return True
            return False

        st = set()
        traverse1(root1, st)
        return traverse2(root2, st, target)
