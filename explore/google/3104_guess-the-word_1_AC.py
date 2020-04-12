# https://leetcode.com/explore/interview/card/google/66/others-4/3104/
# 1AC, ah... it turned out I don't have to make it within 10 attempts
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def numMatch(s1, s2):
            n = len(s1)
            return sum([s1[i] == s2[i] for i in range(n)])

        ws = set(wordlist)
        while len(ws) > 0:
            w = ws.pop()
            cc = master.guess(w)
            if cc == 6:
                return
            ws = set([w1 for w1 in ws if numMatch(w, w1) == cc])
