# medium
# https://leetcode.com/problems/circular-array-loop/
# 1AC, achieving O(1) space is totally feasible, but tricky
# so, forget about it
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        a = nums
        n = len(a)

        def shift(i, x):
            return (i + x) % n if x >= 0 else (i + n + x) % n

        for i in range(n):
            # loop of length 1 is not OK
            if abs(a[i]) % n == 0:
                a[i] = 0

        for i in range(n):
            if a[i] == 0:
                continue

            f = a[i] // abs(a[i])
            j = i
            st = set()
            while True:
                if j in st:
                    return True
                st.add(j)
                if a[j] * f <= 0:
                    break
                x = a[j]
                a[j] = 0
                j = shift(j, x)
        return False
