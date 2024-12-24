# medium
# https://leetcode.com/problems/beautiful-array/
# https://leetcode.com/problems/beautiful-array/discuss/507089/c%2B%2B-6-line-code-100100.
# seriously, I can't tolerate this kind of brain teasers.
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res = [1]
        while len(res) < N:
            res1 = []
            for x in res:
                if 2 * x - 1 <= N:
                    res1.append(2 * x - 1)
            for x in res:
                if 2 * x <= N:
                    res1.append(2 * x)
            res = res1
        return res
