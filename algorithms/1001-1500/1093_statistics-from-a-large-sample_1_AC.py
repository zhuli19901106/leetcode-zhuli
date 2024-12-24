# medium
# https://leetcode.com/problems/statistics-from-a-large-sample/
# not so tough, but rather tiring
from bisect import bisect_left

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        a = count
        na = 256

        i = 0
        while i <= na - 1 and a[i] == 0:
            i += 1
        min_val = 1.0 * i

        i = na - 1
        while i >= 0 and a[i] == 0:
            i -= 1
        max_val = 1.0 * i

        sum_val = 0
        sum_cnt = 0
        mod_val = -1
        mod_cnt = 0
        aq = []
        for i in range(na):
            if a[i] == 0:
                continue
            if a[i] > mod_cnt:
                mod_val = i
                mod_cnt = a[i]
            aq.append((sum_cnt, i))
            sum_cnt += a[i]
            sum_val += i * a[i]
        mean_val = sum_val / sum_cnt

        INT_MAX = 2 ** 31 - 1
        i1 = bisect_left(aq, ((sum_cnt - 1) // 2, INT_MAX)) - 1
        if sum_cnt % 2 == 0:
            i2 = bisect_left(aq, (sum_cnt // 2, INT_MAX)) - 1
            print(aq[i2])
            med_val = (aq[i1][1] + aq[i2][1]) / 2
        else:
            med_val = aq[i1][1] * 1.0

        return [min_val, max_val, mean_val, med_val, mod_val]
