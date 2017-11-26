#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using std::pair;
using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        int n1 = words1.size();
        int n2 = words2.size();
        if (n1 != n2) {
            return false;
        }
        
        unordered_map<string, unordered_set<string>> syn;
        for (auto &p: pairs) {
            syn[p.first].insert(p.second);
            syn[p.second].insert(p.first);
        }
        
        int i;
        for (i = 0; i < n1; ++i) {
            if (words1[i] == words2[i]) {
                continue;
            }
            if (syn.find(words1[i]) == syn.end()) {
                return false;
            }
            if (syn[words1[i]].find(words2[i]) == syn[words1[i]].end()) {
                return false;
            }
        }
        return true;
    }
};
