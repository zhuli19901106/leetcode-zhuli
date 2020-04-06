# https://leetcode.com/problems/split-array-with-equal-sum/
# that's a tricky problem, too tricky to be a "medium".
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        a = nums
        n = len(a)
        if n < 7:
            return False
        ps = [0]
        for i in range(n):
            ps.append(ps[-1] + a[i])

        for j in range(3, n):
            st = set()
            for i in range(1, j - 1):
                sm1 = ps[i] - ps[0]
                sm2 = ps[j] - ps[i + 1]
                if sm1 == sm2:
                    st.add(sm1)
            for k in range(j + 2, n - 1):
                sm1 = ps[k] - ps[j + 1]
                sm2 = ps[n] - ps[k + 1]
                if sm1 == sm2 and sm1 in st:
                    return True
        return False
