# https://leetcode.com/problems/sort-the-jumbled-numbers/
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = [self.mapValue(mapping, x) for x in nums]

        # careful, keep relative order for a tie
        a = list(zip(mapped, range(len(nums)), nums))
        a.sort()

        res = [y for x, i, y in a]
        return res

    def mapValue(self, mapping, x):
        s = [str(mapping[ord(c) - ord('0')]) for c in str(x)]
        s = ''.join(s)
        return int(s)
