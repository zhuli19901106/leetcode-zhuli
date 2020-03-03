# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# careful
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def isSub(sub, par):
            if not sub.startswith(par):
                return False
            ts = sub.split('/')
            tp = par.split('/')
            # key here
            if len(ts) == len(tp):
                return False
            return True

        a = sorted(folder)
        n = len(a)
        res = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and isSub(a[j], a[i]):
                j += 1
            res.append(a[i])
            i = j
        return res
