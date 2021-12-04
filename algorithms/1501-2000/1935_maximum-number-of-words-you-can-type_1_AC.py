# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# 1AC, bit operation

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        m_all = (1 << 26) - 1
        for c in brokenLetters:
            m_all ^= (1 << ord(c) - ord('a'))

        res = 0
        ws = text.split()
        for w in ws:
            m_w = 0
            for c in w:
                m_w |= (1 << ord(c) - ord('a'))
            if (m_w & m_all) == m_w:
                res += 1

        return res
