# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        mask = (1 << k) - 1

        ls = len(s)
        if ls < k:
            return False

        val = 0
        i = 0
        while i < k:
            val = ((val << 1) | (ord(s[i]) - ord('0'))) & mask
            i += 1

        visited = [False for _ in range(mask + 1)]
        cc = mask + 1
        while True:
            if not visited[val]:
                visited[val] = True
                cc -= 1

            if cc == 0:
                return True

            if i >= ls:
                break

            val = ((val << 1) | (ord(s[i]) - ord('0'))) & mask
            i += 1

        return False
