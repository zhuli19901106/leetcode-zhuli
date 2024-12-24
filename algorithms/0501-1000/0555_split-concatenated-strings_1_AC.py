# medium
# https://leetcode.com/problems/split-concatenated-strings/
# https://leetcode.com/problems/split-concatenated-strings/discuss/392359/Python-detailed-explanation
# I came close, but failed to prove the correctness of this solution
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        a = [s if s > s[::-1] else s[::-1] for s in strs]
        max_cur = ''
        for ai, s in enumerate(a):
            ls = len(s)
            a1 = ''.join(a[:ai])
            a2 = ''.join(a[ai + 1:])
            for s1 in (s, s[::-1]):
                for i in range(ls):
                    cur = s1[i:] + a2 + a1 + s1[:i]
                    max_cur = max(max_cur, cur)
        return max_cur
