# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
class Solution:
    def sumZero(self, n: int) -> List[int]:
        a1 = list(range(1, n // 2 + 1))
        a2 = [-x for x in a1]
        a3 = a1 + a2
        if n % 2 == 1:
            a3.append(0)
        return a3
