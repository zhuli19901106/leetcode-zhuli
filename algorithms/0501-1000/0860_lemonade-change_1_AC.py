# easy
# https://leetcode.com/problems/lemonade-change/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m = {5: 0, 10: 0, 20: 0}
        for b in bills:
            m[b] += 1
            if b == 20:
                if m[10] >= 1 and m[5] >= 1:
                    m[10] -= 1
                    m[5] -= 1
                elif m[5] >= 3:
                    m[5] -= 3
                else:
                    return False
            elif b == 10:
                if m[5] >= 1:
                    m[5] -= 1
                else:
                    return False
        return True
