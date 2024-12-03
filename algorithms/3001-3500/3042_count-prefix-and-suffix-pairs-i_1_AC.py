# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res

    def isPrefixAndSuffix(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        for i in range(n1):
            if s1[i] != s2[i]:
                return False
            if s1[n1 - 1 - i] != s2[n2 - 1 - i]:
                return False
        return True
