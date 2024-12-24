# easy
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = self.getScore(player1)
        score2 = self.getScore(player2)
        return 1 if score1 > score2 else 2 if score2 > score1 else 0

    def getScore(self, pins):
        res = 0
        for i, pin in enumerate(pins):
            if (i > 0 and pins[i - 1] == 10) or (i > 1 and pins[i - 2] == 10):
                res += 2 * pin
            else:
                res += pin
        return res
