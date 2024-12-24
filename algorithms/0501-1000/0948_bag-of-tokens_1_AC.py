# medium
# https://leetcode.com/problems/bag-of-tokens/
# 1AC, sort and shrink from both ends
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        a = tokens
        a.sort()
        n = len(a)
        i = 0
        j = n - 1
        pw = P
        max_sc = sc = 0
        while i <= j:
            if pw >= a[i]:
                pw -= a[i]
                sc += 1
                max_sc = max(max_sc, sc)
                i += 1
            elif sc > 0:
                pw += a[j]
                sc -= 1
                j -= 1
            else:
                break
        return max_sc
