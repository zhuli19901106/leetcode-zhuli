# easy
# https://leetcode.com/problems/leaf-similar-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leafSeq(root, seq):
            if root is None:
                return
            if root.left is None and root.right is None:
                seq.append(root.val)
            leafSeq(root.left, seq)
            leafSeq(root.right, seq)

        seq1 = []
        leafSeq(root1, seq1)
        seq2 = []
        leafSeq(root2, seq2)
        if len(seq1) != len(seq2):
            return False
        n = len(seq1)
        for i in range(n):
            if seq1[i] != seq2[i]:
                return False
        return True
