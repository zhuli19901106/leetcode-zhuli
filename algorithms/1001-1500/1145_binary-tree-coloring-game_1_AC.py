# medium
# https://leetcode.com/problems/binary-tree-coloring-game/
# tricky
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        nc = {None: 0}
        nx = None

        def traverse(root):
            nonlocal nc, nx

            if root is None:
                return 0
            if root.val == x:
                nx = root
            c1 = traverse(root.left)
            c2 = traverse(root.right)
            cnt = c1 + c2 + 1
            nc[root] = cnt
            return cnt

        def check(root):
            return nc[root] > n - nc[root]

        traverse(root)
        return check(nx.left) or check(nx.right) or (n - nc[nx]) > nc[nx]
