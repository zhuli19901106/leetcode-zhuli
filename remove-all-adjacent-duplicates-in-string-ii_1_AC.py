# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def remove(s, k):
            res = []
            n = len(s)
            i = 0
            cnt = 0
            while i < n:
                j = i + 1
                while j < n and j - i < k and s[i] == s[j]:
                    j += 1
                if j - i < k:
                    res.append(s[i: j])
                else:
                    cnt += k
                i = j
            return ''.join(res), cnt

        while True:
            s1, cnt = remove(s, k)
            if cnt == 0:
                break
            s = s1
        return s
