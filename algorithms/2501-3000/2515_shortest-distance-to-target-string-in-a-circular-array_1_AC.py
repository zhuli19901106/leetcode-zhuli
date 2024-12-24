# easy
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n):
            if words[(startIndex + i) % n] == target or \
                words[(startIndex + n - i) % n] == target:
                    return i
        return -1
