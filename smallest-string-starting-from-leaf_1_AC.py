# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# 1AC, Runtime: 40 ms, faster than 94.29% of Python3 online submissions for Smallest String Starting From Leaf.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Smallest String Starting From Leaf.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = chr(ord('z') + 1)

        def travese(root, path):
            nonlocal res

            if root.left is None and root.right is None:
                s = ''.join(path)[::-1]
                if s < res:
                    res = s
            if root.left:
                c = chr(ord('a') + root.left.val)
                path.append(c)
                travese(root.left, path)
                path.pop()
            if root.right:
                c = chr(ord('a') + root.right.val)
                path.append(c)
                travese(root.right, path)
                path.pop()

        path = []
        c = chr(ord('a') + root.val)
        path.append(c)
        travese(root, path)
        path.pop()

        return res
