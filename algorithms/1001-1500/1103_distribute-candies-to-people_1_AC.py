# easy
# https://leetcode.com/problems/distribute-candies-to-people/
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        c = candies
        n = num_people
        res = [0 for i in range(n)]
        cc = 1
        i = 0
        while c > 0:
            if c < cc:
                cc = c
            res[i] += cc
            i = (i + 1) % n
            c -= cc
            cc += 1
        return res
