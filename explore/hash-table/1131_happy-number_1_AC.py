# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            if n in st:
                return False
            st.add(n)
            sm = 0
            v = n
            while v != 0:
                sm += (v % 10) ** 2
                v //= 10
            n = sm
        return n == 1
