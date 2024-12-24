# easy
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ls = len(s)
        nw = len(words)
        wi, j = 0, 0
        for i in range(ls):
            if wi >= nw:
                return False
            if s[i] != words[wi][j]:
                return False
            j += 1
            if j == len(words[wi]):
                wi += 1
                j = 0
        return j == 0
