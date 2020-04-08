# https://leetcode.com/explore/interview/card/google/65/design-4/3095/
# that was some tough work... newly-typed sentences will update the trie
from collections import defaultdict
from sortedcontainers import SortedSet

class Trie:
    def __init__(self):
        self.mm = {}
        self.ws = SortedSet()

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.cur = self.root
        self.msc = {}
        self.mcs = defaultdict(set)
        self.buf = []

        n = len(sentences)
        for i in range(n):
            self._insert(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.cur = self.root
            if len(self.buf) > 0:
                self._insert(''.join(self.buf), 1)
                self.buf = []
            return []

        # record the char
        self.buf.append(c)

        if self.cur is None:
            return []

        self.cur = self.cur.mm.get(c, None)
        if self.cur is None:
            return []

        res = [sent for tm, sent in self.cur.ws[:3]]
        return res

    def _insert(self, sent, tm):
        msc = self.msc
        mcs = self.mcs

        if sent in msc:
            self._update(sent, tm)
            return
        msc[sent] = tm
        mcs[tm].add(sent)

        p = self.root
        for i, c in enumerate(sent):
            if not c in p.mm:
                p.mm[c] = Trie()
            p = p.mm[c]
            p.ws.add((-tm, sent))

    def _update(self, sent, tm):
        msc = self.msc
        mcs = self.mcs

        old_tm = msc[sent]
        msc[sent] += tm
        mcs[old_tm].remove(sent)
        if not mcs[old_tm]:
            del mcs[old_tm]
        tm += old_tm
        mcs[tm].add(sent)

        p = self.root
        for i, c in enumerate(sent):
            if not c in p.mm:
                p.mm[c] = Trie()
            p = p.mm[c]
            if (-old_tm, sent) in p.ws:
                p.ws.remove((-old_tm, sent))
            p.ws.add((-tm, sent))

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)