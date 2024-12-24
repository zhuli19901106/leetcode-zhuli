# hard
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# it's actually eaiser to use a stack than to recurse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        s = traversal
        ns = len(s)

        tokens = []
        i = 0
        while i < ns:
            if s[i].isdigit():
                j = i + 1
                while j < ns and s[j].isdigit():
                    j += 1
            else:
                j = i + 1
                while j < ns and s[j] == '-':
                    j += 1
            tokens.append(s[i: j])
            i = j

        st = []
        root = None

        cur_dep = 0
        for tk in tokens:
            if not tk.isdigit():
                cur_dep = len(tk)
                continue

            ptr = TreeNode(int(tk))
            if len(st) == 0:
                st.append(ptr)
                root = ptr
                continue
            while len(st) > cur_dep:
                st.pop()
            par = st[-1]
            if par.left is None:
                par.left = ptr
            else:
                par.right = ptr
            st.append(ptr)

        return st[0] if len(st) > 0 else None
