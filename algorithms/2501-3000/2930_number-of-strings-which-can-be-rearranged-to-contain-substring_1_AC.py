# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/
# how could this be medium? definitely a hard.
# I can't possibly come up with this.
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/solutions/4276730/simple-dynamic-programming-approach-math-wasn-t-mathing-for-me/
class Solution:
    MOD = 1e9 + 7

    def stringCount(self, n: int) -> int:
        if n < 4:
            return 0
        return self.search(n, 1, 2, 1)

    @cache
    def search(self, n, nl, ne, nt):
        if n == 0:
            return 1

        res = 0
        if nl > 0:
            res += self.search(n - 1, nl - 1, ne, nt)
        if ne > 0:
            res += self.search(n - 1, nl, ne - 1, nt)
        if nt > 0:
            res += self.search(n - 1, nl, ne, nt - 1)

        if n > nl + ne + nt:
            nr = 23
            if nl == 0:
                nr += 1
            if ne == 0:
                nr += 1
            if nt == 0:
                nr += 1
            res += nr * self.search(n - 1, nl, ne, nt)

        res %= Solution.MOD
        return int(res)
