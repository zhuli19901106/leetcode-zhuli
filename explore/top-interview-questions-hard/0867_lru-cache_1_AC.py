# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3309/
# kill me with a linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = self

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.mm = {}

    def get(self, key: int) -> int:
        mm = self.mm

        if not key in mm:
            return -1
        p = mm[key]
        res = p.val

        self._detachNode(p)
        self._insertFront(p)

        return res

    def put(self, key: int, value: int) -> None:
        mm = self.mm

        if key in mm:
            p = mm[key]
            p.val = value
            self._detachNode(p)
        else:
            p = Node(key, value)
            if len(mm) == self.cap:
                t = self.head.prev
                self._detachNode(t)
        self._insertFront(p)

    def _insertFront(self, p):
        self.mm[p.key] = p
        if self.head is None:
            self.head = p
            return
        h = self.head
        t = h.prev

        p.next = h
        h.prev = p
        p.prev = t
        t.next = p

        self.head = p

    def _detachNode(self, p):
        del self.mm[p.key]
        if p.next == p:
            self.head = None
            return
        pl = p.prev
        pr = p.next
        pl.next = pr
        pr.prev = pl
        p.prev = p.next = p
        if p == self.head:
            self.head = pr

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
