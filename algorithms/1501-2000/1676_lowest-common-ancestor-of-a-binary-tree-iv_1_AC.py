# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
# post-order traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        st = set()
        for node in nodes:
            st.add(node.val)
        lca_node, cc = self.lca(root, st)
        return lca_node

    def lca(self, root, st):
        if root is None:
            return root, 0

        node_left, cc_left = self.lca(root.left, st)
        if cc_left == len(st):
            return node_left, cc_left
        node_right, cc_right = self.lca(root.right, st)
        if cc_right == len(st):
            return node_right, cc_right

        
        cur = 1 if root.val in st else 0
        cc = cur + cc_left + cc_right
        return root, cc
