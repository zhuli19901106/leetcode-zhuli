# https://leetcode.com/problems/find-unique-binary-string/
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        n2 = 1 << n

        st = set()
        for s in nums:
            x = 0
            for c in s:
                x = (x << 1) | int(c)
            st.add(x)

        x = -1
        for i in range(n2):
            if not i in st:
                x = i
        res = []
        for i in range(n):
            res.append(chr(ord('0') + (x & 1)))
            x >>= 1
        res.reverse()

        return ''.join(res)
