# easy
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        round = min(x, y // 4)
        return 'Alice' if round % 2 == 1 else 'Bob'
