# https://leetcode.com/problems/divisor-game/
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            win = False
            j = 1
            while j * j <= i:
                if i % j != 0:
                    j += 1
                    continue
                if j < i and not dp[i - j]:
                    win = True
                    break
                if i // j < i and not dp[i - i // j]:
                    win = True
                    break
                j += 1
            dp[i] = win
        return dp[N]
