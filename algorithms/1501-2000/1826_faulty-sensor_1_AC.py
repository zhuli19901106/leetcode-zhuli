# easy
# https://leetcode.com/problems/faulty-sensor/
# 1AC, straightforward

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        if len(sensor2) != n:
            return -1

        i = 0
        while i < n:
            if sensor1[i] != sensor2[i]:
                break
            i += 1
        if i == n or i == n - 1:
            return -1

        j = i
        f1 = True
        while j < n - 1:
            if sensor1[j] != sensor2[j + 1]:
                f1 = False
                break
            j += 1
        j = i
        f2 = True
        while j < n - 1:
            if sensor2[j] != sensor1[j + 1]:
                f2 = False
                break
            j += 1

        if f1 ^ f2:
            return 1 if f1 else 2
        else:
            return -1
