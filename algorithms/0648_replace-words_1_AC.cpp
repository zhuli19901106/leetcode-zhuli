// String hashing.
#include <cstdint>
#include <sstream>
#include <unordered_map>
using std::istringstream;
using std::ostringstream;

class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        unordered_map<int64_t, string> um;
        for (auto &w: dict) {
            um[hash(w)] = w;
        }
        
        istringstream is(sentence);
        vector<string> vw;
        string w;
        while (is >> w) {
            vw.push_back(w);
        }
        
        int n = vw.size();
        int i, j;
        int lw;
        int64_t h;
        for (i = 0; i < n; ++i) {
            w = vw[i];
            lw = w.size();
            
            h = 0;
            for (j = 0; j < lw; ++j) {
                h = h * 31 + (w[j] - 'a' + 1);
                if (um.find(h) != um.end()) {
                    vw[i] = um[h];
                    break;
                }
            }
        }
        
        ostringstream os;
        for (i = 0; i < n; ++i) {
            os << vw[i] << ' ';
        }
        string res = os.str();
        res.pop_back();
        
        return res;
    }
private:
    int64_t hash(const string &s) {
        int64_t h = 0;
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            h = h * 31 + (s[i] - 'a' + 1);
        }
        return h;
    }
};
