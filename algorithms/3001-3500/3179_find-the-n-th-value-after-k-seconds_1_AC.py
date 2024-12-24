# medium
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/
# exactly
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = int(1e9 + 7)

        a = [1 for i in range(n)]
        for _ in range(k):
            for i in range(1, n):
                a[i] = (a[i] + a[i - 1]) % MOD
        return a[n - 1]
