# medium
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# pure manual labor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        m_dep = {}
        max_dep = 0

        def depth_traverse(root, dep):
            nonlocal m_dep, max_dep
            
            if root is None:
                return
            max_dep = max(max_dep, dep)
            if not dep in m_dep:
                m_dep[dep] = []
            m_dep[dep].append(root)
            depth_traverse(root.left, dep + 1)
            depth_traverse(root.right, dep + 1)

        depth_traverse(root, 0)

        lca_path = None

        def merge_path(p1, p2):
            if p1 is None:
                return p2[:]
            elif p2 is None:
                return p1[:]
            n = len(p1)
            res = []
            for i in range(n):
                if p1[i] != p2[i]:
                    break
                res.append(p1[i])
            return res

        def lca_traverse(root, path):
            nonlocal m_dep, max_dep, lca_path

            if root is None:
                return
            path.append(root)
            if len(path) == max_dep + 1:
                lca_path = merge_path(lca_path, path)
            lca_traverse(root.left, path)
            lca_traverse(root.right, path)
            path.pop()

        lca_traverse(root, [])
        return lca_path[-1]
