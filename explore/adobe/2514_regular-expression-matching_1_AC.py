# https://leetcode.com/explore/interview/card/apple/347/dynamic-programming/3135/
# rewritten in pythons
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sc, si, sj = [], [], []
        ls, lp = len(s), len(p)

        i = j = 0
        while i < ls or j < lp:
            if j + 1 < lp and p[j + 1] == '*':
                sc.append(p[j])
                si.append(i)
                j += 2
                sj.append(j)
            elif i < ls and j < lp and (p[j] == '.' or s[i] == p[j]):
                i += 1
                j += 1
            elif len(sc) > 0:
                # mismatch
                k = si[-1]
                if k < ls and (sc[-1] == '.' or sc[-1] == s[k]):
                    k += 1
                    i = si[-1] = k
                    j = sj[-1]
                else:
                    # no more possibility
                    sc.pop()
                    si.pop()
                    sj.pop()
            else:
                break
        return i == ls and j == lp
