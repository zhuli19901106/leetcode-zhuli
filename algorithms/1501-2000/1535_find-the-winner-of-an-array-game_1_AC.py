# https://leetcode.com/problems/find-the-winner-of-an-aay-game/
# simulation is acceptable and you don't need a linked list
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        a = arr
        n = len(a)
        if k >= n - 1:
            return max(a)

        cc = 0
        i = 1
        while i < n and cc < k:
            if a[0] > a[i]:
                cc += 1
            else:
                a[0], a[i] = a[i], a[0]
                cc = 1

            i += 1

        return a[0]
