# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# think 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        mp = {}

        def traverse(root, path):
            nonlocal mp

            if root is None:
                return
            mp[root] = path
            if not root.left is None:
                traverse(root.left, path + '0')
            if not root.right is None:
                traverse(root.right, path + '1')

        def diff(p1, p2):
            n1 = len(p1)
            n2 = len(p2)
            i = 0
            while i < n1 and i < n2:
                if p1[i] != p2[i]:
                    break
                i += 1
            return n1 - i + n2 - i

        traverse(root, '')

        pt = mp[target]
        res = []
        for ptr in mp:
            if diff(pt, mp[ptr]) == K:
                res.append(ptr.val)
        return res
