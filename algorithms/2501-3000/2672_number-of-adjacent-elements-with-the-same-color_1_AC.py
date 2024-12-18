# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        a = [0 for i in range(n)]
        res = []

        cc = 0
        for idx, col in queries:
            # overwriting color is possible
            if a[idx] != 0:
                last_col = a[idx]

                if idx - 1 >= 0 and a[idx - 1] == last_col:
                    cc -= 1
                if idx + 1 <= n - 1 and a[idx + 1] == last_col:
                    cc -= 1

            a[idx] = col
            if idx - 1 >= 0 and a[idx - 1] == col:
                cc += 1
            if idx + 1 <= n - 1 and a[idx + 1] == col:
                cc += 1

            res.append(cc)
        return res
