# https://leetcode.com/problems/vowels-game-in-a-string/
# this is BS
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vw = set('aeiou')
        cc = len([c for c in s if c in vw])
        return cc > 0
