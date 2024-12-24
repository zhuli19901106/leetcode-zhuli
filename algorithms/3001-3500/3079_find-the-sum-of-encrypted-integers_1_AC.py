# easy
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([self.encryptDigit(x) for x in nums])

    def encryptDigit(self, x):
        nd, mx = 0, 0
        while x != 0:
            mx = max(mx, x % 10)
            x //= 10
            nd += 1
        return (10 ** nd - 1) // 9 * mx
