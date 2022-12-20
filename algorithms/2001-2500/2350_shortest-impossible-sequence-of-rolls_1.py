# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
# quite the reverse thinking

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 0
        st = set()
        for x in rolls:
            if x in st:
                continue
            st.add(x)

            # a whole group of 1-k is collected
            if len(st) == k:
                st = set()
                res += 1

        return res + 1
