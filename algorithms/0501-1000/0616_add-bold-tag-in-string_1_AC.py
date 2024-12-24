# medium
# https://leetcode.com/problems/add-bold-tag-in-string/
# 1AC, trie solution, intuitive and tolerable
class Trie:
    def __init__(self):
        self.nodes = {}
        self.word = False
    
    def insert(self, w):
        p = self
        for i, c in enumerate(w):
            if not c in p.nodes:
                p.nodes[c] = Trie()
            p = p.nodes[c]
        p.word = True

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        dt = dict
        del dict

        tr = Trie()
        for w in dt:
            tr.insert(w)

        mt = set()
        n = len(s)
        for i in range(n):
            p = tr
            j = i
            k = -1
            while j < n and p:
                if not s[j] in p.nodes:
                    break
                p = p.nodes[s[j]]
                if p.word:
                    k = j
                j += 1
            if k == -1:
                continue
            while k >= i:
                mt.add(k)
                k -= 1
        res = []
        i = 0
        while i < n:
            if not i in mt:
                res.append(s[i])
                i += 1
                continue

            res.append('<b>')
            j = i
            while j < n and j in mt:
                j += 1
            res.append(s[i: j])
            res.append('</b>')
            i = j
        return ''.join(res)
