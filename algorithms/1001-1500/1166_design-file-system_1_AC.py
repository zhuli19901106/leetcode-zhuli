# medium
# https://leetcode.com/problems/design-file-system/
# 1AC
class FileSystem:
    def __init__(self):
        self.mm = {}

    def createPath(self, path: str, value: int) -> bool:
        mm = self.mm
        if path in mm:
            return False
        i = path.rfind('/')
        parent_path = path[: i]
        if i > 0 and not parent_path in mm:
            return False
        mm[path] = value
        return True

    def get(self, path: str) -> int:
        mm = self.mm
        return mm.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)