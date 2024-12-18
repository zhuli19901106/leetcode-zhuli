# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
# just search it, careful with the search order
from sortedcontainers import SortedSet

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2 * n - 1
        a = [0 for i in range(m)]

        st = SortedSet(range(1, n + 1))
        self.search(0, st, a, m)
        return a

    def search(self, idx, st, a, m):
        if len(st) == 0:
            return True

        while idx < m and a[idx] != 0:
            idx += 1
        if idx >= m:
            return False

        for i in range(len(st) - 1, -1 , -1):
            x = st[i]

            if x == 1:
                a[idx] = x
                st.remove(x)

                ret = self.search(idx + 1, st, a, m)
                if ret:
                    return True

                st.add(x)
                a[idx] = 0
                continue

            if idx + x > m - 1 or a[idx + x] != 0:
                continue

            a[idx] = a[idx + x] = x
            st.remove(x)

            ret = self.search(idx + 1, st, a, m)
            if ret:
                return True

            st.add(x)
            a[idx] = a[idx + x] = 0

        return False
