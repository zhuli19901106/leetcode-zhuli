# medium
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/
# BF
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ['0', '1']
        for i in range(n - 1):
            res1 = []
            for s in res:
                if s[-1] == '1':
                    res1.append(s + '0')
                res1.append(s + '1')
            res = res1
        return res
