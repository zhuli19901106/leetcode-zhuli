# easy
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        aw = words
        aa = [''.join(sorted(w)) for w in aw]
        while True:
            found = False
            for i in range(1, len(aw)):
                if aa[i] == aa[i - 1]:
                    del aw[i]
                    del aa[i]
                    found = True
                    break
            if not found:
                break
        return aw
