# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# took me too long to figure out the sliding window

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def slide(s, k, c1, c2):
            res = 0

            n = len(s)
            i1, i2 = 0, 0
            ck = 0
            while i1 < n:
                while i2 < n:
                    if s[i2] == c1:
                        i2 += 1
                    else:
                        i2 += 1
                        ck += 1

                    if ck <= k:
                        res = max(res, i2 - i1)
                    else:
                        break
                
                while i1 < i2 and s[i1] != c2:
                    i1 += 1
                i1 += 1
                ck -= 1
                res = max(res, i2 - i1)

                if i2 == n:
                    break

            return res

        return max(slide(answerKey, k, 'T', 'F'), slide(answerKey, k, 'F', 'T'))
