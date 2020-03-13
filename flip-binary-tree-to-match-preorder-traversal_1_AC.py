# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# a bit tricky, though
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []

        def traverse(root, idx):
            nonlocal res

            if root is None:
                return True, idx - 1
            if root.val != voyage[idx]:
                return False, idx

            for i in range(2):
                ret1 = ret2 = False
                ret1, idx1 = traverse(root.left, idx + 1)
                if ret1:
                    ret2, idx2 = traverse(root.right, idx1 + 1)
                if ret1 and ret2:
                    return True, idx2
                if i > 0:
                    break
                root.left, root.right = root.right, root.left
                res.append(root.val)
            return False, idx

        ret, _ = traverse(root, 0)
        if ret:
            return res
        else:
            return [-1]
