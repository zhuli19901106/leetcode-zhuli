# easy
# https://leetcode.com/problems/fair-candy-swap/
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sa = sum(A)
        sb = sum(B)
        diff = (sa - sb) // 2
        sta = set(A)
        stb = set(B)
        for xa in sta:
            if (xa - diff) in stb:
                return [xa, xa - diff]
        return None
