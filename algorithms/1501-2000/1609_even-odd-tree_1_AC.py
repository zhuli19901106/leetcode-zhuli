# https://leetcode.com/problems/even-odd-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        res = []
        self.traverse(root, 0, res)
        print(res)
        for i in range(len(res)):
            if i % 2 == 0:
                for j, x in enumerate(res[i]):
                    if x % 2 != 1 or (j > 0 and res[i][j - 1] >= x):
                        return False
            else:
                for j, x in enumerate(res[i]):
                    if x % 2 != 0 or (j > 0 and res[i][j - 1] <= x):
                        return False
        return True

    def traverse(self, root, depth, res):
        if len(res) <= depth:
            res.append([])
        res[depth].append(root.val)

        if root.left:
            self.traverse(root.left, depth + 1, res)
        if root.right:
            self.traverse(root.right, depth + 1, res)
