# https://leetcode.com/problems/uncommon-words-from-two-sentences/class Solution:
'''
Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
'''
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        def count(sen):
            ws = sen.strip().split()
            s = set(ws)
            m = {}
            for w in ws:
                if not w in m:
                    m[w] = 1
                else:
                    m[w] += 1
            return m, s

        m1, s1 = count(A)
        m2, s2 = count(B)
        s12 = s1 - s2
        s21 = s2 - s1
        res = []
        for w in s12:
            if m1[w] == 1:
                res.append(w)
        for w in s21:
            if m2[w] == 1:
                res.append(w)
        return res
