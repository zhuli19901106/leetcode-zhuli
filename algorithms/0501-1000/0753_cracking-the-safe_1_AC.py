# hard
# https://leetcode.com/problems/cracking-the-safe/
# https://leetcode.com/problems/cracking-the-safe/discuss/441235/10-line-python-concise-DFS-code
# extremely concise and delicate code
from collections import defaultdict

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join([chr(ord('0') + i) for i in range(k)])

        mm = defaultdict(lambda: (1 << k) - 1)
        res = []

        def dfs(s):
            nonlocal res, mm

            while mm[s] != 0:
                v = mm[s]
                idx = str(k - (v & -v).bit_length())
                v &= v - 1
                mm[s] = v
                dfs(s[1:] + idx)
                res.append(idx)

        dfs(str(k - 1) * (n - 1))
        return ''.join(res + [str(k - 1)] * (n - 1))
