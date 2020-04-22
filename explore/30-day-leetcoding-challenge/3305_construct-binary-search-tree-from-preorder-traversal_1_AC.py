# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3305/
# 1AC, needs a bit thinking.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        a = preorder
        n = len(a)
        if n == 0:
            return None

        r = TreeNode(a[0])
        st = [r]
        for i in range(1, n):
            p = TreeNode(a[i])
            if len(st) == 0:
                st.append(p)
                continue

            p0 = st[-1]
            if p.val < p0.val:
                p0.left = p
                st.append(p)
                continue
            while len(st) > 1 and p.val > st[-2].val:
                st.pop()
            st[-1].right = p
            st.pop()
            st.append(p)
        return r
