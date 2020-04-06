# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/discuss/553595/O(n)-time-and-O(1)-space-solution
# I was close, but got confused at some point
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    INT_MAX = 2 ** 31 - 1

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        md, mv = Solution.INT_MAX, -1

        def dfs2(root, dp):
            nonlocal md, mv

            if root is None:
                return
            if root.left is None and root.right is None:
                if dp < md:
                    md, mv = dp, root.val
            dfs2(root.left, dp + 1)
            dfs2(root.right, dp + 1)

        def dfs1(root):
            nonlocal md, mv

            if root is None:
                return 0
            if root.val == k:
                dfs2(root, 0)
                # return backtrack distance for parent
                return 1

            ll = dfs1(root.left)
            if ll > 0:
                ll += 1
                dfs2(root.right, ll)
                return ll

            rr = dfs1(root.right)
            if rr > 0:
                rr += 1
                dfs2(root.left, rr)
                return rr

            return 0

        dfs1(root)
        return mv
