# medium
# https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        n = len(pushed)
        st = []
        while j < n:
            if len(st) > 0 and st[-1] == popped[j]:
                st.pop()
                j += 1
            elif i < n:
                st.append(pushed[i])
                i += 1
            else:
                break
        return i == n and j == n and len(st) == 0
