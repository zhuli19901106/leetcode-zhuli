# medium
# https://leetcode.com/problems/last-stone-weight-ii/
# split by two and make the diff as small as possible
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        st = set()
        st.add(0)
        total = sum(stones)
        lim = total // 2
        f = 1
        nf = 1 - f
        for x in stones:
            for i in range(lim, x - 1, -1):
                if i - x in st:
                    st.add(i)
        i = lim
        while i > 0 and not i in st:
            i -= 1
        return (total - i) - i
