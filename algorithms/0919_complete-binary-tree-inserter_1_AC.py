# https://leetcode.com/problems/complete-binary-tree-inserter/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.n = CBTInserter._count(root)

    def insert(self, v: int) -> int:
        self.n += 1
        idx = self.n
        path = bin(idx)[3:]
        last = None
        ptr = self.root
        for c in path:
            last = ptr
            if c == '0':
                ptr = ptr.left
            else:
                ptr = ptr.right
        ptr = TreeNode(v)
        if path[-1] == '0':
            last.left = ptr
        else:
            last.right = ptr
        return last.val

    def get_root(self) -> TreeNode:
        return self.root

    @staticmethod
    def _count(root):
        if root is None:
            return 0
        return 1 + CBTInserter._count(root.left) +\
            CBTInserter._count(root.right)

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()