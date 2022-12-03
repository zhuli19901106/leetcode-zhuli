# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        st = set()
        for i in range(n - 2):
            if num[i + 2] == num[i + 1] and num[i + 1] == num[i]:
                st.add(num[i: i + 3])
        good = sorted(st)

        return good[-1] if len(good) > 0 else ''
