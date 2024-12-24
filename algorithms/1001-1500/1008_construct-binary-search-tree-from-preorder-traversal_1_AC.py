# medium
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        a = preorder
        if len(a) == 0:
            return None
        root = TreeNode(a[0])
        st = []
        st.append(root)
        n = len(a)
        for i in range(1, n):
            if a[i] < st[-1].val:
                ptr = TreeNode(a[i])
                st[-1].left = ptr
                st.append(ptr)
                continue

            if a[i] == st[-1].val:
                continue

            ptr = TreeNode(a[i])
            if len(st) == 1:
                st[-1].right = ptr
                st.pop()
                st.append(ptr)
                continue

            while len(st) >= 2 and a[i] > st[-2].val:
                st.pop()
            ptr1 = st.pop()
            ptr1.right = ptr
            st.append(ptr)
        return root
