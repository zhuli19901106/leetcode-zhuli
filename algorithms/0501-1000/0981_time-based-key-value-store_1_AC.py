# medium
# https://leetcode.com/problems/time-based-key-value-store/
# 1AC, since the timestamps are increasing, that's one less problem to worry about
from bisect import bisect_right
class TimeMap:
    NULL_VAL = ''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        ds = self.ds
        if not key in ds:
            ds[key] = []
        ds[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ds = self.ds
        if not key in ds:
            return TimeMap.NULL_VAL
        a = ds[key]
        n = len(a)
        i = bisect_right(a, (timestamp + 1, '')) - 1
        return a[i][1] if i >= 0 else TimeMap.NULL_VAL

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)