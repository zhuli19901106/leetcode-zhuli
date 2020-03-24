// Sliding window + string hashing
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    Solution() {
        pw.push_back(1);
    }
    
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        
        auto &w = words;
        int nw = w.size();
        int ls = s.size();
        if (nw == 0 || ls == 0) {
            return res;
        }
        
        unordered_map<int64_t, int> cnt1;
        int lw = w[0].size();
        int64_t hw = 0;
        int i, j;
        for (i = 0; i < nw; ++i) {
            hw = 0;
            for (j = 0; j < lw; ++j) {
                hw = hw * P + (w[i][j] - 'a' + 1);
            }
            ++cnt1[hw];
        }
        
        vector<int64_t> hs(ls + 2, 0);
        for (i = 1; i <= ls; ++i) {
            hs[i] = hs[i - 1] * P + (s[i - 1] - 'a' + 1);
        }
        
        unordered_map<int64_t, int> cnt2;
        int k;
        int64_t old_hw;
        for (k = 0; k < lw; ++k) {
            i = k;
            j = i + lw;
            while (i < ls && j <= ls) {
                hw = hash(hs, j - lw + 1, j);
                if (cnt1.find(hw) == cnt1.end()) {
                    // No such word
                    i = j;
                    j = i + lw;
                    cnt2.clear();
                    continue;
                }
                
                ++cnt2[hw];
                if (j - i == nw * lw && cnt2[hw] == cnt1[hw]) {
                    res.push_back(i);
                }
                while (j - i == nw * lw || cnt2[hw] > cnt1[hw]) {
                    old_hw = hash(hs, i + 1, i + lw);
                    --cnt2[old_hw];
                    i += lw;
                }
                
                j += lw;
            }
            cnt2.clear();
        }
        sort(res.begin(), res.end());
        
        hs.clear();
        cnt1.clear();
        cnt2.clear();
        
        return res;
    }
    
    ~Solution() {
        pw.clear();
    }
private:
    static const int64_t P = 31;
    vector<int64_t> pw;
    
    int64_t getPow(int i) {
        while (pw.size() <= i) {
            pw.push_back(pw.back() * P);
        }
        return pw[i];
    }
    
    int64_t hash(vector<int64_t> &h, int left, int right) {
        return h[right] - h[left - 1] * getPow(right - left + 1);
    }
};
