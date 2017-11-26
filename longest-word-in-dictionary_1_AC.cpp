// If it's linear, it's iterative.
#include <algorithm>
#include <string>
#include <unordered_set>
using std::sort;
using std::string;
using std::unordered_set;

bool comparator(const string &s1, const string &s2)
{
    if (s1.size() != s2.size()) {
        return s1.size() < s2.size();
    } else {
        return s1 < s2;
    }
}

class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end(), comparator);
        
        unordered_set<string> hou;
        hou.insert("");
        
        string max_w = "";
        string s;
        for (auto &w: words) {
            s = w;
            
            s.pop_back();
            if (hou.find(s) == hou.end()) {
                continue;
            }
            // zici
            hou.insert(w);
            if (w.size() > max_w.size()) {
                max_w = w;
            }
        }
        
        return max_w;
    }
};
