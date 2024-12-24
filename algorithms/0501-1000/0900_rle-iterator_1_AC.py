# medium
# https://leetcode.com/problems/rle-iterator/
# Runtime: 24 ms, faster than 100.00% of Python3 online submissions for RLE Iterator.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for RLE Iterator.
class RLEIterator:
    def __init__(self, A: List[int]):
        self.idx = 0
        self.cnt = 0
        arr = []
        n = len(A)
        for i in range(0, n, 2):
            if A[i] == 0:
                continue
            arr.append((A[i + 1], A[i]))
        self.arr = arr

    def next(self, n: int) -> int:
        if n <= 0:
            return -1
        while n > 0 and self.idx < len(self.arr):
            res = self.arr[self.idx][0]
            diff = self.arr[self.idx][1] - self.cnt
            if n >= diff:
                self.idx += 1
                self.cnt = 0
                n -= diff
            else:
                self.cnt += n
                n = 0
        return res if n == 0 else -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)