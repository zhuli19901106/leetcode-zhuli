# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s
        s1 = []
        for i in range(0, n, k):
            cur_s = s[i: i + k] if i + k <= n else s[i:]
            s1.append(str(sum(map(int, list(cur_s)))))
        s1 = ''.join(s1)

        return self.digitSum(s1, k)
