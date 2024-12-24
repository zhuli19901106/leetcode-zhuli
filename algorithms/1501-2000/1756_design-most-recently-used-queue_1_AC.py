# medium
# https://leetcode.com/problems/design-most-recently-used-queue/
# random access and shifting can't be satisfied at the same time

class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MRUQueue:    
    def __init__(self, n: int):
        self.n = n
        h, t = None, None
        for i in range(1, n + 1):
            p = Node(i)
            if h is None:
                h = t = p
                h.next = h
                h.prev = h
                continue

            t.next = p
            p.prev = t
            t = p

            t.next = h
            h.prev = t
        self.head, self.tail = h, t

    def fetch(self, k: int) -> int:
        if self.head is None:
            return None

        h, t = self.head, self.tail
        if k == 1:
            h, t = h.next, t.next
        elif k != self.n:
            p = h
            for i in range(k - 1):
                p = p.next
            p1, p2 = p.prev, p.next
            p1.next = p2
            p2.prev = p1

            t.next = p
            p.prev = t
            t = p

            t.next = h
            h.prev = t

        self.head, self.tail = h, t
        return self.tail.val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)