# medium
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
# a striaghtforward iteration using set will TLE
# it's consecutive and start from 0, actually easier
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        '''
        # TLE
        st = {0}
        idx = 1
        for x in coins:
            # if x is already beyond current missing number, stop
            if x > idx:
                break

            st1 = set()
            for y in st:
                if not x + y in st:
                    st1.add(x + y)

            st |= st1
            while idx in st:
                idx += 1
        return idx
        '''

        idx = 0
        for x in coins:
            if x > idx + 1:
                break
            idx += x
        return idx + 1
