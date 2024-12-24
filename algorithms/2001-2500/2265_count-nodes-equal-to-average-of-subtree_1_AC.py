# medium
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0, False, 0, 0

            sm_left, _, tot_left, cnt_left = traverse(root.left)
            sm_right, _, tot_right, cnt_right = traverse(root.right)

            sm = root.val + sm_left + sm_right
            tot = tot_left + tot_right + 1
            f = (sm // tot == root.val)
            cnt = cnt_left + cnt_right + (1 if f else 0)

            return sm, f, tot, cnt

        if root is None:
            return 0
        _, _, _, res = traverse(root)

        return res
