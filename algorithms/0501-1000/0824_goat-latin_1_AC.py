# easy
# https://leetcode.com/problems/goat-latin/
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vw = set('aeiouAEIOU')
        res = []
        for i, w in enumerate(S.strip().split(' ')):
            aaa = 'a' * (i + 1)
            if w[0] in vw:
                w1 = w + 'ma' + aaa
            else:
                w1 = w[1:] + w[0] + 'ma' + aaa
            res.append(w1)
        return ' '.join(res)
