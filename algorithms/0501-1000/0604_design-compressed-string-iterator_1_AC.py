# https://leetcode.com/problems/design-compressed-string-iterator/
class StringIterator:
    def __init__(self, compressedString: str):
        s = compressedString
        self.cs = []
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            j = i + 1
            cc = 0
            while j < n and s[j].isdigit():
                cc = cc * 10 + ord(s[j]) - ord('0')
                j += 1
            self.cs.append((ch, cc))
            i = j
        self.ich = 0
        self.icc = 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        ch = self.cs[self.ich][0]
        self.icc += 1
        if self.icc == self.cs[self.ich][1]:
            self.ich += 1
            self.icc = 0
        return ch

    def hasNext(self) -> bool:
        return self.ich < len(self.cs)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()