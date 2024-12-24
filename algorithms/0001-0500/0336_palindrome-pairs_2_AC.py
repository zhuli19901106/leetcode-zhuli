# hard
# https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1055/
# after the OJ adjusted the time limit, this problem became pointless
# you can beat it with a brute-force solution but TLE with an optimized one
# that's a joke
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ws = words
        if len(ws) == 0:
            return []

        res = []
        mm = {w: i for i, w in enumerate(ws)}

        for i, w in enumerate(ws):
            for j in range(len(w) + 1):
                s1, s2 = w[:j], w[j:]
                if self.pal(s1):
                    tmp = s2[::-1]
                    if tmp in mm and mm[tmp] != i:
                        res.append([mm[tmp], i])
                if len(s2) > 0 and self.pal(s2):
                    tmp = s1[::-1]
                    if tmp in mm and mm[tmp] != i:
                        res.append([i, mm[tmp]])
        return res

    def pal(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
