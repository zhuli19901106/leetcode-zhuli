# medium
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    def __init__(self, root: TreeNode):
        self.vals = set()
        self.recover(root, 0)

    def recover(self, root, val):
        if root is None:
            return
        root.val = val
        self.vals.add(val)
        self.recover(root.left, 2 * val + 1)
        self.recover(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
