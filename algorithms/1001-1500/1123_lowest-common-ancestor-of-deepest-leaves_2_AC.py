# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# cleaner solution from post order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class NodeInfo:
    def __init__(self, dep, lca_node):
        self.dep = dep
        self.lca_node = lca_node

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        def traverse(root, dep):
            if root.left is None and root.right is None:
                return NodeInfo(dep, root)

            nl = None
            if not root.left is None:
                nl = traverse(root.left, dep + 1)
            nr = None
            if not root.right is None:
                nr = traverse(root.right, dep + 1)

            if nl is None:
                return nr
            elif nr is None:
                return nl
            elif nl.dep > nr.dep:
                return nl
            elif nl.dep < nr.dep:
                return nr
            else:
                return NodeInfo(nl.dep, root)

        res = traverse(root, 0)
        return res.lca_node
