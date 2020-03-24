#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        auto &vs = strings;
        int n = vs.size();
        
        unordered_map<string, vector<string>> um;
        string s1;
        for (auto &s: vs) {
            s1 = shift(s);
            um[s1].push_back(s);
        }
        
        vector<vector<string>> res;
        for (auto it = um.begin(); it != um.end(); ++it) {
            res.push_back(it->second);
        }
        um.clear();
        
        return res;
    }
private:
    static const int DICT_SIZE = 26;
    
    string shift(string s) {
        int ls = s.size();
        if (ls == 0 || s[0] == 'z') {
            return s;
        }
        
        string s1 = s;
        int off = 'z' - s[0];
        int i;
        for (i = 0; i < ls; ++i) {
            s1[i] = (s1[i] - 'a' + off) % DICT_SIZE + 'a';
        }
        return s1;
    }
};
