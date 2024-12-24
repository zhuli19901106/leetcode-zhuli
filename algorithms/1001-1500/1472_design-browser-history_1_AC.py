# medium
# https://leetcode.com/problems/design-browser-history/
# 1AC, easy does it
class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.st = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        while len(self.st) > self.idx + 1:
            self.st.pop()
        self.st.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx -= min(self.idx, steps)
        return self.st[self.idx]

    def forward(self, steps: int) -> str:
        self.idx += min(len(self.st) - 1 - self.idx, steps)
        return self.st[self.idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)