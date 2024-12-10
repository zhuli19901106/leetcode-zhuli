# https://leetcode.com/problems/cousins-in-binary-tree-ii/
# tricky
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        sm = []
        self.calcSum(root, 1, sm)

        root.val = 0
        self.traverse(root, 1, sm)

        return root

    def calcSum(self, root, depth, sm):
        if root.left:
            self.calcSum(root.left, depth + 1, sm)
        if root.right:
            self.calcSum(root.right, depth + 1, sm)

        while len(sm) < depth:
            sm.append(0)
        sm[depth - 1] += root.val

    def traverse(self, root, depth, sm):
        if root.left is None and root.right is None:
            return

        if root.left:
            self.traverse(root.left, depth + 1, sm)
        if root.right:
            self.traverse(root.right, depth + 1, sm)

        vl = root.left.val if root.left else 0
        vr = root.right.val if root.right else 0
        if root.left:
            root.left.val = sm[depth] - vl - vr
        if root.right:
            root.right.val = sm[depth] - vl - vr
