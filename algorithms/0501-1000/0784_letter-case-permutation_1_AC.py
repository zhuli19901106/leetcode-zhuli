# medium
# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(s, w, i, n, res):
            print(w)
            if i == n:
                res.append(''.join(w))
                return
            w.append(s[i])
            dfs(s, w, i + 1, n, res)
            w.pop()
            if s[i] >= 'a' and s[i] <= 'z':
                w.append(s[i].upper())
                dfs(s, w, i + 1, n, res)
                w.pop()

        res = []
        dfs(S.lower(), [], 0, len(S), res)
        return res
