# https://leetcode.com/problems/positions-of-large-groups/
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        s = S
        n = len(s)
        i = j = 0
        while j < n:
            if i < n and s[i] == s[j]:
                i += 1
            else:
                if i - j >= 3:
                    res.append([j, i - 1])
                j = i
        return res
