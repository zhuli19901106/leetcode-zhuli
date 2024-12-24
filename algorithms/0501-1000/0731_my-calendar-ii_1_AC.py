# medium
# https://leetcode.com/problems/my-calendar-ii/
# do we really have to write segment tree in a real interview?
# this is the ugliest code I've ever written.
# segment tree with split and merge
class SegTreeNode:
    def __init__(self, x, y, val=0):
        self.x = x
        self.y = y
        self.val = val
        self.left = self.right = None

class SegTree:
    NULL_VAL = -1

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.root = SegTreeNode(start, end)

    def insert(self, x, y, val):
        self._insert(x, y, self.root, val)

    def _insert(self, x, y, root, val):
        ex, ey = root.x, root.y
        if y <= ex or x >= ey:
            return
        if x == ex and y == ey and\
            not root.left and not root.right:
            root.val += val
            return

        mid = ex + (ey - ex) // 2
        res = 0

        if not root.left:
            root.left = SegTreeNode(ex, mid, root.val if root.val != SegTree.NULL_VAL else 0)
        if not root.right:
            root.right = SegTreeNode(mid, ey, root.val if root.val != SegTree.NULL_VAL else 0)

        if x < mid:
            self._insert(x, min(mid, y), root.left, val)
        if y > mid:
            self._insert(max(mid, x), y, root.right, val)

        if not root.left or not root.right:
            root.val = SegTree.NULL_VAL
            return
        if root.left and root.right:
            lv = root.left.val
            rv = root.right.val
            if lv == SegTree.NULL_VAL or rv == SegTree.NULL_VAL or lv != rv:
                root.val = SegTree.NULL_VAL
            else:
                # merge intervals if possible
                root.val = lv
                root.left = root.right = None

    def query(self, x, y):
        return self._query(x, y, self.root)
    
    def _query(self, x, y, root):
        ex, ey = root.x, root.y
        if y <= ex or x >= ey:
            return 0
        if x >= ex and y <= ey and\
            not root.left and not root.right:
            return root.val
        mid = ex + (ey - ex) // 2

        lv = 0
        if x < mid and root.left:
            lv = self._query(x, min(mid, y), root.left)
        rv = 0
        if y > mid and root.right:
            rv = self._query(max(mid, x), y, root.right)
        return max(lv, rv)

    @staticmethod
    def traverse(root):
        if not root:
            return
        if root.val != -1:
            print((root.x, root.y, root.val), end='')
        SegTree.traverse(root.left)
        SegTree.traverse(root.right)

class MyCalendarTwo:

    def __init__(self):
        self.sgt = SegTree(0, 2 ** 31)

    def book(self, start: int, end: int) -> bool:
        mx = self.sgt.query(start, end)
        if mx >= 2:
            return False
        self.sgt.insert(start, end, 1)
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)