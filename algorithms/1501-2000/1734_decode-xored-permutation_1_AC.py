# https://leetcode.com/problems/decode-xored-permutation/
# n is odd
# more of a gimmick than analytical thinking

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        sm = 0
        for i in range(1, n + 1):
            sm ^= i
        val = 0
        for i in range(0, n - 1, 2):
            val ^= encoded[i]

        perm = [0 for i in range(n)]
        perm[n - 1] = sm ^ val
        for i in range(n - 2, -1, -1):
            perm[i] = encoded[i] ^ perm[i + 1]

        return perm
