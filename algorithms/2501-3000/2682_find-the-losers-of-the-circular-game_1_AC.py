# easy
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        st = set()
        i = 0

        x = 1
        st.add(x)
        i += 1

        while True:
            x1 = (x + i * k - 1) % n + 1
            if x1 in st:
                break
            x = x1
            st.add(x)
            i += 1

        res = []
        for i in range(1, n + 1):
            if not i in st:
                res.append(i)
        return res
