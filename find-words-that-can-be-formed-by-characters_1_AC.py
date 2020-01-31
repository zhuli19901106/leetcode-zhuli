# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([len(w) for w in words if self.isGood(chars, w)])

    def isGood(self, s, t):
        ss = sorted(s)
        tt = sorted(t)
        ls = len(ss)
        lt = len(tt)
        i = 0
        j = 0
        while i < ls and j < lt:
            if ss[i] == tt[j]:
                j += 1
            i += 1
        return j == lt
