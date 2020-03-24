# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4 * x + 2 * y = v1
        # x + y = v2
        NULL_VAL = []
        v1, v2 = tomatoSlices, cheeseSlices
        if v1 % 2 != 0:
            return NULL_VAL
        v1 //= 2
        x = v1 - v2
        y = v2 - x
        if x < 0 or y <  0:
            return NULL_VAL
        return [x, y]
