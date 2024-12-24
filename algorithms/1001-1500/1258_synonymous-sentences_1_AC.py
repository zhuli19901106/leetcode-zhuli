# medium
# https://leetcode.com/problems/synonymous-sentences/
# 1AC, not difficult, but a bit tiring
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        synset = [set(ws) for ws in synonyms]
        synset_ds = []
        while len(synset) > 0:
            cur = synset.pop()
            i = 0
            while i < len(synset):
                if synset[i] & cur:
                    cur |= synset[i]
                    del synset[i]
                else:
                    i += 1
            synset_ds.append(cur)
        synset = synset_ds
        synset = [sorted(ws) for ws in synset]

        mi = {}
        for i, ws in enumerate(synset):
            for w in ws:
                mi[w] = i

        res = []
        text = text.split(' ')

        def dfs(idx, sen):
            nonlocal res

            if idx == len(text):
                res.append(' '.join(sen))
                return
            if text[idx] in mi:
                i = mi[text[idx]]
                for w in synset[i]:
                    sen.append(w)
                    dfs(idx + 1, sen)
                    sen.pop()
            else:
                sen.append(text[idx])
                dfs(idx + 1, sen)
                sen.pop()

        dfs(0, [])
        return res
