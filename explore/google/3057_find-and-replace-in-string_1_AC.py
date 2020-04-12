# https://leetcode.com/problems/find-and-replace-in-string/
# add-hoc, per se
class Solution:
    def findReplaceString(self, S: str, indexes: List[int],\
        sources: List[str], targets: List[str]) -> str:
        ls = len(S)
        n = len(indexes)
        mm = {}
        for i in range(n):
            mm[indexes[i]] = (sources[i], targets[i])

        res = []
        i = 0
        while i < ls:
            if not i in mm:
                res.append(S[i])
                i += 1
                continue

            j = 0
            src, tg = mm[i]
            ns = len(src)
            while j < ns and i + j < ls:
                if S[i + j] != src[j]:
                    break
                j += 1

            if j == ns:
                res.append(tg)
                i += ns
            else:
                res.append(S[i])
                i += 1
        return ''.join(res)
