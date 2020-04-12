# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# 1AC, not very fast, but intuitive
# n-ary version
#       1
#       │
#    ┌──┼──┐
#    │  │  │
#    2  3  4
# binary version
# 1--x--x--x
#    |  |  |
#    2  3  4
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if root is None:
            return None

        tr = TreeNode(root.val)
        if len(root.children) == 0:
            return tr

        tp = tr
        for c in root.children:
            tp.right = TreeNode(None)
            tp = tp.right
            tp.left = self.encode(c)
        return tr

	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        tr = data
        if tr is None:
            return None

        root = Node(tr.val)
        root.children = []
        p = tr
        while p.right:
            p = p.right
            root.children.append(self.decode(p.left))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
