# https://leetcode.com/problems/sort-vowels-in-a-string/
class Solution:
    def sortVowels(self, s: str) -> str:
        vw = set('AEIOUaeiou')
        av = []
        for c in s:
            if c in vw:
                av.append(c)
        av.sort()

        t = []
        j = 0
        for c in s:
            if c in vw:
                t.append(av[j])
                j += 1
            else:
                t.append(c)
        t = ''.join(t)
        return t
