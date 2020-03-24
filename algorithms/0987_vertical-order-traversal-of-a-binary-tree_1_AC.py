# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# supposed to be 1AC
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def traverse(root, mm, x, y):
            if root is None:
                return
            if not x in mm:
                mm[x] = set()
            mm[x].add((-y, root.val))
            traverse(root.left, mm, x - 1, y - 1)
            traverse(root.right, mm, x + 1, y - 1)

        mm = {}
        traverse(root, mm, 0, 0)
        ak = sorted(mm.keys())

        res = []
        for k in ak:
            res.append([x[1] for x in sorted(mm[k])])
        return res
