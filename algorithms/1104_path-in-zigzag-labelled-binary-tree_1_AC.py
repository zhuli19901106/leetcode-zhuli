# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
from math import log2

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(log2(label))

        start, end = 2 ** level, 2 ** (level + 1) - 1
        if level % 2 == 1:
            v = start + end - label
        else:
            v = label

        res = []
        for i in range(level, -1, -1):
            start, end = 2 ** i, 2 ** (i + 1) - 1
            if i % 2 == 1:
                res.append(start + end - v)
            else:
                res.append(v)
            v //= 2
        return res[::-1]
