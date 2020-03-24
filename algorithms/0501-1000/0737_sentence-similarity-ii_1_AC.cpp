#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    bool areSentencesSimilarTwo(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        if (words1.size() != words2.size()) {
            return false;
        }
        
        unordered_map<string, string> dj;
        string r1, r2;
        for (auto &p: pairs) {
            r1 = findRoot(dj, p.first);
            r2 = findRoot(dj, p.second);
            if (r1 != r2) {
                dj[r1] = r2;
            }
        }
        
        int n = words1.size();
        int i;
        for (i = 0; i < n; ++i) {
            r1 = findRoot(dj, words1[i]);
            r2 = findRoot(dj, words2[i]);
            if (r1 != r2) {
                break;
            }
        }
        dj.clear();
        
        return i == n;
    }
private:
    string findRoot(unordered_map<string, string> &dj, string x) {
        if (dj.find(x) == dj.end()) {
            dj[x] = x;
            return x;
        }
        
        string r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        string k = x;
        while (x != r) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
