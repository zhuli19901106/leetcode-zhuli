# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        np = len(players)
        nt = len(trainers)

        res = 0
        i, j = 0, 0
        while i < np and j < nt:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1

        return res
