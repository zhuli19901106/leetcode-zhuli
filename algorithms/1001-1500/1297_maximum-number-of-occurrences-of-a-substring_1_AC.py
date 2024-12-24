# medium
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# brute-force
# I got some minor optimizations to spare, but can't think of any wise solutions
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        mm = {}
        for i in range(n - minSize + 1):
            ss = s[i: i + minSize]
            if len(set(ss)) > maxLetters:
                continue
            if ss in mm:
                mm[ss] += 1
            else:
                mm[ss] = 1
        if len(mm) == 0:
            return 0
        return max(mm.values())
