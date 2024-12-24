# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# so, maybe, just BF
from collections import defaultdict

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        MAXC = 26

        mm_letters = defaultdict(lambda: 0)
        for c in letters:
            mm_letters[c] += 1

        a_words = []
        for w in words:
            mw = {}
            sc = 0
            for c in w:
                sc += score[ord(c) - ord('a')]
                if not c in mw:
                    mw[c] = 0
                mw[c] += 1
            a_words.append((w, mw, sc))

        res = [0]
        self.search(0, 0, a_words, mm_letters, res)
        return res[0]

    def search(self, idx, cur_score, a_words, mm_letters, res):
        if idx == len(a_words):
            res[0] = max(res[0], cur_score)
            return

        w, mw, sc = a_words[idx]

        self.search(idx + 1, cur_score, a_words, mm_letters, res)

        enough = True
        for c in mw:
            if mm_letters[c] < mw[c]:
                enough = False
                break
        if not enough:
            return

        for c in mw:
            mm_letters[c] -= mw[c]
        self.search(idx + 1, cur_score + sc, a_words, mm_letters, res)
        for c in mw:
            mm_letters[c] += mw[c]
