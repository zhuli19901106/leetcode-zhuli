# medium
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# there're only 26 * 26 combinations, very limited
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        MAXC = 26
        sa = ''.join([chr(ord('a') + i) for i in range(MAXC)])
        marks = set()
        m1, m2 = {}, {}

        n = len(s)
        for i in range(1, n):
            if not s[i] in m2:
                m2[s[i]] = 1
            else:
                m2[s[i]] += 1

        for i in range(1, n - 1):
            c0, c1 = s[i - 1], s[i]

            if not c0 in m1:
                m1[c0] = 1
            else:
                m1[c0] += 1

            m2[c1] -= 1
            if m2[c1] == 0:
                del m2[c1]

            for c in sa:
                if not (c in m1 and c in m2):
                    continue
                marks.add(c1 + c)

        return len(marks)
