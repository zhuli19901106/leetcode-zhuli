# easy
# https://leetcode.com/problems/apple-redistribution-into-boxes/
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        sm = sum(apple)

        res = 0
        for c in capacity:
            sm -= c
            res += 1
            if sm <= 0:
                break
        return res
