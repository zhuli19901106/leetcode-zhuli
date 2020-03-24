# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# just search it
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        a = [s for s in arr if len(s) == len(set(s))]
        sta = [set(s) for s in a]
        n = len(a)
        max_len = 0

        def dfs(idx, st, cur_len):
            nonlocal max_len
            if cur_len > max_len:
                max_len = cur_len
            if idx == n:
                return
            if len(sta[idx] & st) == 0:
                dfs(idx + 1, sta[idx] | st, cur_len + len(a[idx]))
            dfs(idx + 1, st, cur_len)

        dfs(0, set(), 0)
        return max_len
