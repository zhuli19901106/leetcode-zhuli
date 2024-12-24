# medium
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# longest common prefix must happen at some alphabetically adjacent cases
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a = []
        for x in arr1:
            a.append((str(x), 0))
        for x in arr2:
            a.append((str(x), 1))
        a.sort()

        res = 0
        n = len(a)
        for i in range(n - 1):
            if a[i][1] == a[i + 1][1]:
                continue
            s1, s2 = a[i][0], a[i + 1][0]
            n1, n2 = len(s1), len(s2)

            cc = 0
            while cc < n1 and cc < n2 and s1[cc] == s2[cc]:
                cc += 1
            res = max(res, cc)

        return res
