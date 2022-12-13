# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
# I got sloppy on this one
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def traverse(root, dep, mm_par, mm_dep, st_leaf):
            if root is None:
                return
            if root.left is None and root.right is None:
                st_leaf.add(root.val)

            mm_dep[root.val] = dep
            traverse(root.left, dep + 1, mm_par, mm_dep, st_leaf)
            if root.left:
                mm_par[root.left.val] = root.val

            traverse(root.right, dep + 1, mm_par, mm_dep, st_leaf)
            if root.right:
                mm_par[root.right.val] = root.val

        def lcaPath(x, y, mm_par, mm_dep):
            dx, dy = mm_dep[x], mm_dep[y]
            if dx < dy:
                return lcaPath(y, x, mm_par, mm_dep)

            cnt = 0
            while dx > dy:
                x = mm_par[x]
                dx -= 1
                cnt += 1
            while x != y:
                x = mm_par[x]
                y = mm_par[y]
                dx -= 1
                dy -= 1
                cnt += 2
            return x, cnt

        mm_par = {}
        mm_dep = {}
        st_leaf = set()
        traverse(root, 0, mm_par, mm_dep, st_leaf)
        # which nodes are possible candidates?
        nodes = list(st_leaf)
        nodes.append(root.val)

        res = 0
        for cur in nodes:
            _, cnt = lcaPath(cur, start, mm_par, mm_dep)
            res = max(res, cnt)

        return res
