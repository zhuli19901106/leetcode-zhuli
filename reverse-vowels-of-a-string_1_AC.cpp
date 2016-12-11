#include <algorithm>
#include <unordered_set>
using std::swap;
using std::unordered_set;

class Solution {
public:
    Solution() {
        string v = "aeiouAEIOU";
        int n = v.size();
        int i;
        for (i = 0; i < n; ++i) {
            vowel.insert(v[i]);
        }
    }
    
    string reverseVowels(string s) {
        int n = s.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            if (!isVowel(s[i])) {
                ++i;
            } else if (!isVowel(s[j])) {
                --j;
            } else {
                swap(s[i++], s[j--]);
            }
        }
        return s;
    }
    
    ~Solution() {
        vowel.clear();
    }
private:
    unordered_set<char> vowel;
    
    bool isVowel(char ch) {
        return vowel.find(ch) != vowel.end();
    }
};
