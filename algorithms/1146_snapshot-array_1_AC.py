# https://leetcode.com/problems/snapshot-array/
# 1AC, chain changes by ascending version number for each slot, then binary search
from bisect import bisect_right

class SnapshotArray:
    INT_MAX = 2 ** 31 - 1

    def __init__(self, length: int):
        self.n = length
        self.a = []
        self.ver = 0
        for i in range(self.n):
            # (version, val)
            self.a.append([(self.ver, 0)])

    def set(self, index: int, val: int) -> None:
        old_val = self.a[index][-1][1]
        if val == old_val:
            return
        self.a[index].append((self.ver + 1, val))

    def snap(self) -> int:
        self.ver += 1
        return self.ver - 1

    def get(self, index: int, snap_id: int) -> int:
        ai = self.a[index]
        m = len(ai)
        i = bisect_right(ai, (snap_id + 1, SnapshotArray.INT_MAX)) - 1
        return ai[i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)