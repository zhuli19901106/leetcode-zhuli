# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# simple idea, a bit tough to write it clean, though
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwap(a):
            n = len(a)
            a1 = sorted(a)
            mm = {}
            for i, x in enumerate(a1):
                mm[x] = i
            idx = [mm[x] for x in a]

            res = 0
            for i in range(n):
                if idx[i] == i:
                    continue
                x = idx[i]
                while x != idx[x]:
                    x = idx[i]
                    y = idx[x]
                    idx[x] = x
                    idx[i] = y

                    x = i
                    res += 1

            return res

        def traverse(root, dep, nodes):
            if root is None:
                return

            if dep >= len(nodes):
                nodes.append([])
            nodes[dep].append(root.val)
            traverse(root.left, dep + 1, nodes)
            traverse(root.right, dep + 1, nodes)

        nodes = []
        traverse(root, 0, nodes)
        res = 0
        for lvl in nodes:
            res += minSwap(lvl)

        return res
