# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def traverse(root, path, ap):
            if root.left is None and root.right is None:
                ap.append(path)
                return
            if root.left:
                traverse(root.left, path + '0', ap)
            if root.right:
                traverse(root.right, path + '1', ap)

        ap = []
        traverse(root, '', ap)

        res = 0
        n = len(ap)
        for i in range(n):
            for j in range(i + 1, n):
                ni = len(ap[i])
                nj = len(ap[j])
                k = 0
                while k < ni and k < nj:
                    if ap[i][k] != ap[j][k]:
                        break
                    k += 1
                sp = (ni - k) + (nj - k)
                if sp <= distance:
                    res += 1

        return res
