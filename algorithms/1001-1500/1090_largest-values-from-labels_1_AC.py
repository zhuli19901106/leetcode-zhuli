# medium
# https://leetcode.com/problems/largest-values-from-labels/
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int],\
        num_wanted: int, use_limit: int) -> int:
        a = sorted(zip(values, labels), key=lambda x: -x[0])
        ml = {}
        res = 0
        cnt = 0
        for x in a:
            if cnt >= num_wanted:
                break
            if x[1] in ml:
                if ml[x[1]] >= use_limit:
                    continue
                ml[x[1]] += 1
                res += x[0]
                cnt += 1
            else:
                ml[x[1]] = 1
                res += x[0]
                cnt += 1
        return res
