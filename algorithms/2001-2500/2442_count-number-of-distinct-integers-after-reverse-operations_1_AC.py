# medium
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverseDigits(x):
            x1 = 0
            while x != 0:
                x1 = x1 * 10 + x % 10
                x //= 10
            return x1

        st = set()
        for x in nums:
            st.add(x)
            st.add(reverseDigits(x))

        return len(st)
