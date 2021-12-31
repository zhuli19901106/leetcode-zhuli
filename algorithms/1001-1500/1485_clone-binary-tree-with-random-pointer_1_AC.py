# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/
# 1AC, can't think of a solution without hashing the nodes

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # hashing an object is the wrong thing to do
        node_map = {}
        root1 = self.copyTree(root, node_map)
        self.recoverRandom(root1, node_map)

        return root1

    def copyTree(self, root, node_map):
        if root is None:
            return None
        root1 = NodeCopy(root.val)
        node_map[root] = root1
        root1.left = self.copyTree(root.left, node_map)
        root1.right = self.copyTree(root.right, node_map)
        root1.random = root.random

        return root1

    def recoverRandom(self, root, node_map):
        if root is None:
            return
        rand_node = root.random
        if rand_node:
            root.random = node_map[rand_node]
        self.recoverRandom(root.left, node_map)
        self.recoverRandom(root.right, node_map)
