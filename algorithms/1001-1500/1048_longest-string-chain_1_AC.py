# medium
# https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ws = list(set(words))
        ws.sort(key=lambda x: len(x))

        def isPred(s1, s2):
            if len(s1) + 1 != len(s2):
                return False
            i = j = 0
            n = len(s1)
            nd = 0
            while j < n + 1:
                if i < n and s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    nd += 1
                if nd > 1:
                    return False
            return True

        dp = {}
        for w in ws:
            nw = len(w)
            if not nw in dp:
                dp[nw] = {}
            dp[nw][w] = 1
            if not nw - 1 in dp:
                continue
            for w1 in dp[nw - 1]:
                if not isPred(w1, w):
                    continue
                dp[nw][w] = max(dp[nw][w], dp[nw - 1][w1] + 1)
        res = 0
        for n in dp:
            res = max(res, max(dp[n].values()))
        return res
