# medium
# https://leetcode.com/problems/construct-smallest-number-from-di-string/
# searching

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        lp = len(pattern)

        def dfs(val, idx, st):
            if idx == len(pattern):
                return val

            d = val % 10
            rg = range(d + 1, 10) if pattern[idx] == 'I' else range(1, d)
            for d1 in rg:
                if d1 in st:
                    continue
                st.add(d1)
                cur_val = dfs(val * 10 + d1, idx + 1, st)
                st.remove(d1)
                if cur_val != -1:
                    return cur_val

            return -1

        res = -1
        st = set()
        for i in range(1, 10):
            st.add(i)
            res = dfs(i, 0, st)
            st.remove(i)
            if res != -1:
                break

        return str(res)
