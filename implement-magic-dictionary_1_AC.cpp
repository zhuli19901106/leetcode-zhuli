// The lookup can be accelerated by string hashing.
#include <string>
#include <unordered_set>
using std::string;
using std::unordered_set;

class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {}
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for (string &s: dict) {
            us.insert(s);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        int lw = word.size();
        if (lw == 0) {
            return 0;
        }
        int i, j;
        char c;
        for (i = 0; i < lw; ++i) {
            c = word[i];
            for (j = 0; j < 26; ++j) {
                if (c == 'a' + j) {
                    continue;
                }
                word[i] = 'a' + j;
                if (us.find(word) != us.end()) {
                    return true;
                }
            }
            word[i] = c;
        }
        return false;
    }
    
    ~MagicDictionary() {
        us.clear();
    }
private:
    unordered_set<string> us;
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */
