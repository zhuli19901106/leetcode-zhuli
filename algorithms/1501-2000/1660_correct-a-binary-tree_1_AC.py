# https://leetcode.com/problems/correct-a-binary-tree/
# 1AC, level order traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        q = deque()
        st = set()

        q.append((None, root, 0))
        st.add(root)
        found = False
        while len(q) > 0:
            par, cur, direc = q.pop()
            if cur.left:
                if cur.left in st:
                    found = True
                    break
                q.append((cur, cur.left, 0))
                st.add(cur.left)
            if cur.right:
                if cur.right in st:
                    found = True
                    break
                q.append((cur, cur.right, 1))
                st.add(cur.right)
        if not found:
            return root
        if direc == 0:
            par.left = None
        else:
            par.right = None
        return root
