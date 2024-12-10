# https://leetcode.com/problems/string-compression-iii/
# should be easy
class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        n = len(word)

        i = 0
        while i < n:
            j = i + 1
            while j < n and j - i < 9 and word[j] == word[i]:
                j += 1
            res.append('{}{}'.format(j - i, word[i]))
            i = j
        res = ''.join(res)
        return res
