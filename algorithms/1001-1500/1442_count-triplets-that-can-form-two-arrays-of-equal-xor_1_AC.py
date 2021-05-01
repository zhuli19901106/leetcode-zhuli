# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
# 1AC, quite easy after a bit thinking
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ax = [0]
        for x in arr:
            ax.append(ax[-1] ^ x)

        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if ax[i] == ax[j]:
                    res += j - i - 1
        return res
