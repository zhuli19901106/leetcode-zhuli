# https://leetcode.com/problems/count-vowel-strings-in-ranges/
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vw = set('aeiou')
        a = [int(w[0] in vw and w[-1] in vw) for w in words]
        sm = [0]
        for x in a:
            sm.append(sm[-1] + x)

        res = []
        for x, y in queries:
            res.append(sm[y + 1] - sm[x])
        return res
