# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
# 1AC, I know, recursive solution, but why bother
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        st = []
        p = head
        while p:
            st.append(p)
            p = p.getNext()
        n = len(st)
        for i in range(n - 1, -1, -1):
            st[i].printValue()
