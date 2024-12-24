# medium
# https://leetcode.com/problems/design-memory-allocator/
# actual memory allocation algorithms are extremely non-trivial, or super hard
# I can't believe I spent over 1 hour coding this and got it one-shot
class Allocator:

    def __init__(self, n: int):
        self.free = [[0, n]]
        self.alloc = {}

    def allocate(self, size: int, mID: int) -> int:
        # look for free blocks
        nf = len(self.free)
        i = 0
        while i < nf:
            xf, yf = self.free[i]
            if yf - xf < size:
                i += 1
                continue

            xa, ya = xf, xf + size
            if yf - xf > size:
                xf += size
                self.free[i] = [xf, yf]
            else:
                del self.free[i]
            break
        if i == nf:
            return -1

        if not mID in self.alloc:
            self.alloc[mID] = []

        # check for insert position
        al = self.alloc[mID]
        na = len(al)
        j = 0
        while j < na and xa >= al[j][1]:
            j += 1
        j -= 1

        # check if two blocks can be joined to one
        bl = (j > -1 and xa == al[j][1])
        br = (j + 1 < na and ya == al[j + 1][0])

        if bl:
            if br:
                al[j][1] = al[j + 1][1]
                del al[j + 1]
            else:
                al[j][1] = ya
        elif br:
            al[j + 1][0] = xa
        else:
            al.insert(j + 1, [xa, ya])

        return xa

    def freeMemory(self, mID: int) -> int:
        if not mID in self.alloc:
            return 0

        size = 0
        fr = self.free
        al = self.alloc[mID]
        for xa, ya in al:
            nf = len(fr)
            i = 0
            while i < nf and xa >= fr[i][1]:
                i += 1
            i -= 1

            # check if two blocks can be joined to one
            bl = (i > -1 and xa == fr[i][1])
            br = (i + 1 < nf and ya == fr[i + 1][0])

            if bl:
                if br:
                    fr[i][1] = fr[i + 1][1]
                    del fr[i + 1]
                else:
                    fr[i][1] = ya
            elif br:
                fr[i + 1][0] = xa
            else:
                fr.insert(i + 1, [xa, ya])

            size += ya - xa
        del self.alloc[mID]

        return size

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)