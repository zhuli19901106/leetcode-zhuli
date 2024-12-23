# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# sliding window
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        st = set()
        
        res = -1
        j = 0
        for i, x in enumerate(cards):
            found = False
            if x in st:
                found = True

            while x in st:
                st.remove(cards[j])
                j += 1

            st.add(x)
            if found and res == -1 or res > i - j + 1:
                res = i - j + 2

        return res
