# https://leetcode.com/problems/merge-strings-alternately/
# 1AC
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        res = []
        for i in range(min(n1, n2)):
            res.append(word1[i])
            res.append(word2[i])
        if n1 >= n2:
            res.append(word1[n2:])
        else:
            res.append(word2[n1:])
        return ''.join(res)
