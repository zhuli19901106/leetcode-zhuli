# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for x in arr:
            if not x in m:
                m[x] = 0
            m[x] += 1
        counts = m.values()
        return len(counts) == len(set(counts))
