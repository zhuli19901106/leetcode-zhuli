# easy
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# 1AC, use a stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        res = [0 for i in range(len(prices))]
        for i, x in enumerate(prices):
            if len(st) == 0 or x > st[-1][1]:
                st.append((i, x))
                continue
            while len(st) > 0 and x <= st[-1][1]:
                res[st[-1][0]] = st[-1][1] - x
                st.pop()
            st.append((i, x))

        while len(st) > 0:
            res[st[-1][0]] = st[-1][1]
            st.pop()
        return res
