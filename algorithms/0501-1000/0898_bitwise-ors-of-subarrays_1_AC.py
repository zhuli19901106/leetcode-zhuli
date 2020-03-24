# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# it's basically brute-force, but let's hope there're more duplicates.
class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur = [set() for i in range(2)]
        res = set()

        f = 1
        nf = 1 - f
        for x in A:
            cur[f] = set()
            cur[f].add(x)
            for y in cur[nf]:
                cur[f].add(x | y)
            res |= cur[f]
            f = 1 - f
            nf = 1 - f
        return len(res)
