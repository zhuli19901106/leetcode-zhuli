# medium
# https://leetcode.com/problems/ip-to-cidr/
# 1AC, what kind of "easy" is this?
from math import log2

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ipToInt(s):
            a = [int(x) for x in s.split('.')[::-1]]
            res = 0
            for i, x in enumerate(a):
                res |= (x << 8 * i)
            return res

        def intToIp(ip):
            res = []
            for i in range(4):
                res.append(str((ip >> 8 * i) & 0xff))
            return '.'.join(res[::-1])

        ip = ipToInt(ip)
        res = []
        while n > 0:
            d1 = ip & -ip
            d2 = 1 << ((n).bit_length() - 1)
            d = min(d1, d2)
            b = int(log2(d))
            res.append('{}/{}'.format(intToIp(ip), 32 - b))
            ip += d
            n -= d
        return res
