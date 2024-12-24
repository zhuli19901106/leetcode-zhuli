# medium
# https://leetcode.com/problems/linked-list-in-binary-tree/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def traverseLocal(root, head):
            if head is None:
                return True
            if root is None or root.val != head.val:
                return False
            return traverseLocal(root.left, head.next) or\
                traverseLocal(root.right, head.next)

        if root is None:
            return False
        if root.val == head.val and traverseLocal(root, head):
            return True
        return self.isSubPath(head, root.left) or\
            self.isSubPath(head, root.right)
