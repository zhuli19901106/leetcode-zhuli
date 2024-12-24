# easy
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        a = matrix
        n = len(a)

        for i in range(n):
            st = set()
            for j in range(n):
                val = a[i][j]
                if val < 1 or val > n:
                    return False
                if val in st:
                    return False
                st.add(val)
            if len(st) != n:
                return False

        for i in range(n):
            st = set()
            for j in range(n):
                val = a[j][i]
                if val < 1 or val > n:
                    return False
                if val in st:
                    return False
                st.add(val)
            if len(st) != n:
                return False

        return True
