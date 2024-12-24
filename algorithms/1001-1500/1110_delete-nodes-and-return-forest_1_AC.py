# medium
# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        st_del = set(to_delete)
        res = []

        def traverse(root):
            nonlocal st_del, res

            if root is None:
                return root
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            if root.val in st_del:
                if not root.left is None:
                    res.append(root.left)
                if not root.right is None:
                    res.append(root.right)
                return None
            return root

        root = traverse(root)
        if not root is None:
            res.append(root)
        return res
