# medium
# https://leetcode.com/problems/car-pooling/
# after trying many finicky method, I settled for a stupid but clean solution.
# brute-force
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a = trips
        a.sort(key=lambda x: (x[1], x[2]))
        st = set()
        for x in a:
            st.add(x[1])
            st.add(x[2])
        ap = sorted(list(st))
        np = len(ap) - 1
        cp = [0 for i in range(np)]
        j = 0
        for x in a:
            while j < np and ap[j + 1] <= x[1]:
                j += 1
            k = 0
            while j + k < np and ap[j + k] < x[2]:
                cp[j + k] += x[0]
                k += 1
        for x in cp:
            if x > capacity:
                return False
        return True
