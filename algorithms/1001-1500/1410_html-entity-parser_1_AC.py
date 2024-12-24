# medium
# https://leetcode.com/problems/html-entity-parser/
# just BF
class Solution:
    def entityParser(self, text: str) -> str:
        enc = ['&quot;', '&apos;', '&amp;', '&gt;', '&lt;', '&frasl;']
        lenc = [len(p) for p in enc]
        ne = len(enc)

        dec = ['"', '\'', '&', '>', '<', '/']
        mm = dict(zip(enc, dec))

        s = text
        ns = len(s)
        i = 0
        mt = []
        while i < ns:
            if s[i] != '&':
                i += 1
                continue

            found = False
            for j in range(ne):
                if i + lenc[j] <= ns and s[i: i + lenc[j]] == enc[j]:
                    mt.append((i, j))
                    found = True
                    i += lenc[j]
            if not found:
                i += 1

        res = []
        i, k = 0, 0
        while i < ns:
            if k == len(mt) or i != mt[k][0]:
                res.append(s[i])
                i += 1
                continue

            j = mt[k][1]
            i += lenc[j]
            k += 1
            res.append(dec[j])
        res = ''.join(res)
        return res
