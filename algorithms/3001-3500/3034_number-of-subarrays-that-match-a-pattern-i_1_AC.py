# medium
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
# sort of like KMP match (and rematch after mismatch)
# just BF for now
# better yet, convert it to "abc" for [-1, 0, 1] to do a string match
# watch for overlapping matches
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        sn = []
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                sn.append('a')
            elif nums[i] > nums[i + 1]:
                sn.append('c')
            else:
                sn.append('b')
        sn = ''.join(sn)

        sp = []
        for p in pattern:
            if p == +1:
                sp.append('a')
            elif p == -1:
                sp.append('c')
            else:
                sp.append('b')
        sp = ''.join(sp)

        # overlapping matches
        return len(re.findall('(?=({}))'.format(sp), sn))
