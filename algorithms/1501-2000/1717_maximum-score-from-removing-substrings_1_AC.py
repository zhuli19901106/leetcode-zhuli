# medium
# https://leetcode.com/problems/maximum-score-from-removing-substrings/
# paused for 20 minutes and couldn't figure out why it's greedy
# this should be a tricky "hard"
# tried various methods, finally worked after 1+ hour
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        n = len(s)
        i = 0
        while i < n:
            if not (s[i] == 'a' or s[i] == 'b'):
                i += 1
            t = []
            j = i
            while j < n and (s[j] == 'a' or s[j] == 'b'):
                t.append(s[j])
                j += 1
            t = ''.join(t)

            res += self.check(t, x, y)
            i = j
        return res

    def check(self, s, x, y):
        res = 0
        if x > y:
            c1, s1 = self.removeSubstring(s, x, 'ab')
            c2, s2 = self.removeSubstring(s1, y, 'ba')
        else:
            c1, s1 = self.removeSubstring(s, y, 'ba')
            c2, s2 = self.removeSubstring(s1, x, 'ab')
        res = c1 + c2
        return res

    def removeSubstring(self, s, x, p):
        res = 0
        st = []
        for c in s:
            st.append(c)
            if len(st) >= 2 and st[-2] == p[0] and st[-1] == p[1]:
                res += x
                st.pop()
                st.pop()
        return res, ''.join(st)
