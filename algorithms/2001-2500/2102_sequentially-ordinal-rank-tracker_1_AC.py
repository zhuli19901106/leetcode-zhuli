# hard
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/
from bisect import bisect_right

class SORTracker:

    def __init__(self):
        self.idx_query = 0
        self.arr = []

    def add(self, name: str, score: int) -> None:
        tp = (-score, name)
        i = bisect_right(self.arr, tp)
        self.arr.insert(i, tp)

    # somewhat ridiculous to fix the query index
    def get(self) -> str:
        res = self.arr[self.idx_query]
        self.idx_query += 1

        return res[1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
