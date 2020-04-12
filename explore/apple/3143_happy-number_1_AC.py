# https://leetcode.com/explore/interview/card/apple/348/others/3143/
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
