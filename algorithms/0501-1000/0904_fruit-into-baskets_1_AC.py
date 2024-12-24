# medium
# https://leetcode.com/problems/fruit-into-baskets/
# sliding window to record unique values, my code was too ugly to read
# very misleading description, though
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        j = 0
        mm = {}
        mc = 0

        n = len(tree)
        i = j = 0
        res = 0
        while i < n:
            while i < n and mc <= 2:
                ch = tree[i]
                if not ch in mm:
                    mm[ch] = 0
                if mm[ch] == 0:
                    mc += 1
                mm[ch] += 1
                i += 1
            if mc <= 2:
                res = max(res, i - j)
                continue
            res = max(res, i - j - 1)
            while j < i:
                ch = tree[j]
                mm[ch] -= 1
                j += 1
                if mm[ch] == 0:
                    mc -= 1
                    break
        return res
