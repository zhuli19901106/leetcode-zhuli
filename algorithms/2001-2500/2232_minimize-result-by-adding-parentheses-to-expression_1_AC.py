# medium
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution:
    def minimizeResult(self, expression: str) -> str:
        s = expression
        ls = len(s)
        idx_sign = s.find('+')

        min_val = 1 << 31 - 1
        res = ''
        for i in range(0, idx_sign):
            s1 = s[:i]
            n1 = int(s1) if len(s1) > 0 else 1

            s2 = s[i:idx_sign]
            n2 = int(s2)
            for j in range(idx_sign + 1, ls):
                s3 = s[idx_sign + 1: j + 1]
                n3 = int(s3)

                s4 = s[j + 1:]
                n4 = int(s4) if len(s4) > 0 else 1

                cur = n1 * (n2 + n3) * n4
                if cur < min_val:
                    min_val = cur
                    res = f'{s1}({s2}+{s3}){s4}'

        return res
