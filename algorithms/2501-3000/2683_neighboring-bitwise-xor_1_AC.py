# medium
# https://leetcode.com/problems/neighboring-bitwise-xor/
# flip every element and you get the same xor result
# so, it doesn't matter
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        a = [0 for i in range(n)]
        for i in range(n - 1):
            a[i + 1] = a[i] ^ derived[i]
        return a[0] == a[n - 1] ^ derived[n - 1]
