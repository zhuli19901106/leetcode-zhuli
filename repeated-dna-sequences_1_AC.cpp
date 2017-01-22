// ACGT = 0123, quite convenient for bit compression.
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    Solution() {
        i_to_a = "ACGT";
        int ls = i_to_a.size();
        int i;
        for (i = 0; i < ls; ++i) {
            a_to_i[i_to_a[i]] = i;
        }
    }
    
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        int ls = s.size();
        if (ls < DNA_LEN) {
            return res;
        }
        
        unordered_map<int, int> um;
        int i;
        int val;
        
        i = 0;
        val = 0;
        while (i < DNA_LEN) {
            val = ((val << 2) & ((1 << 2 * DNA_LEN) - 1) | a_to_i[s[i]]);
            ++i;
        }
        ++um[val];
        while (i < ls) {
            val = ((val << 2) & ((1 << 2 * DNA_LEN) - 1) | a_to_i[s[i]]);
            ++um[val];
            ++i;
        }
        for (auto it = um.begin(); it != um.end(); ++it) {
            if (it->second >= 2) {
                res.push_back(deserialize(it->first));
            }
        }
        um.clear();
        return res;
    }
    
    string deserialize(int x) {
        int i = 2 * (DNA_LEN - 1);
        string s = "";
        while (i >= 0) {
            s.push_back(i_to_a[(x >> i) & 3]);
            i -= 2;
        }
        return s;
    }
private:
    static const int DNA_LEN = 10;
    string i_to_a;
    unordered_map<char, int> a_to_i;
};
