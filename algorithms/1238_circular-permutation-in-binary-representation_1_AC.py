# https://leetcode.com/problems/circular-permutation-in-binary-representation/
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        a = Solution.grayCode(n)
        #for i, x in enumerate(a):
        #    if x == start:
        #        idx = i
        #        break
        
        # binary search
        idx = Solution.search(0, (1 << n) - 1, n, start, False)
        return a[idx:] + a[:idx]

    @staticmethod
    def search(i, j, n, val, reverse):
        if i == j:
            return i
        b = ((val & (1 << n - 1)) != 0)
        mid = i + (1 << n - 1)

        i1, j1 = (mid, j) if b ^ reverse else (i, mid - 1)
        if b:
            reverse = not reverse
        return Solution.search(i1, j1, n - 1, val, reverse)

    @staticmethod
    def grayCode(n):
        a = [0, 1]
        for ni in range(1, n):
            b2 = 2 ** ni
            a1 = []
            for i in range(b2):
                a1.append(a[i])
            for i in range(b2 - 1, -1 , -1):
                a1.append(b2 + a[i])
            a = a1
        return a
