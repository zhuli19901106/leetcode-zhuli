# medium
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# 1AC, a bit convoluted, but still manageable
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.dfs(root, set())

    def dfs(self, root, st):
        if not root.val in st:
            st.add(root.val)
        else:
            st.remove(root.val)

        if root.left is None and root.right is None:
            res = 1 if len(st) <= 1 else 0
        else:
            res = 0
            if root.left:
                res += self.dfs(root.left, st)
            if root.right:
                res += self.dfs(root.right, st)

        if root.val in st:
            st.remove(root.val)
        else:
            st.add(root.val)
        return res
