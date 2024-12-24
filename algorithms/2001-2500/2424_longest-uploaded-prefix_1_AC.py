# medium
# https://leetcode.com/problems/longest-uploaded-prefix/
# amortized O(1)
class LUPrefix:

    def __init__(self, n: int):
        self.st = set()
        self.cur = 0

    def upload(self, video: int) -> None:
        self.st.add(video)
        if not video == self.cur + 1:
            return
        while self.cur + 1 in self.st:
            self.cur += 1

    def longest(self) -> int:
        return self.cur


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()