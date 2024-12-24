# easy
# https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mc_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
            "...","-","..-","...-",".--","-..-","-.--","--.."]
        mc_dict = dict(zip(map(lambda x: chr(ord('a') + x), range(26)), mc_list))
        code_words = [''.join([mc_dict[c] for c in w]) for w in words]
        return len(set(code_words))
