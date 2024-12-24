# medium
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# simple idea, but takes a while to implement
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if root is None:
            return ''

        par = {}
        self.calcParent(root, par)

        a1, p1 = self.getPath(startValue, par)
        a2, p2 = self.getPath(destValue, par)
        n1 = len(a1)
        n2 = len(a2)
        i = 0
        while i < n1 - 1 and i < n2 - 1 and a1[i + 1] == a2[i + 1]:
            i += 1

        s1 = p1[i:]
        s2 = p2[i:]

        if len(s1) == 0:
            return s2
        elif len(s2) == 0:
            return 'U' * len(s1)
        else:
            return 'U' * len(s1) + s2

    def calcParent(self, root, par):
        if root.left:
            par[root.left.val] = (root.val, 0)
            self.calcParent(root.left, par)

        if root.right:
            par[root.right.val] = (root.val, 1)
            self.calcParent(root.right, par)

    def getPath(self, x0, par):
        x = x0

        nodes = [x]
        path = []
        while x in par:
            p, d = par[x]
            nodes.append(p)
            path.append(d)
            x = p
        nodes.reverse()
        path.reverse()
        path = ''.join(['L' if d == 0 else 'R' for d in path])

        return nodes, path
