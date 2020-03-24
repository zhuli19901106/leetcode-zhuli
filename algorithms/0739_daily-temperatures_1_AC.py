# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        a = T
        n = len(T)
        st = []
        res = [0 for i in range(n)]
        for i in range(n):
            while len(st) > 0 and a[st[-1]] < a[i]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        while len(st) > 0:
            st.pop()
        return res
