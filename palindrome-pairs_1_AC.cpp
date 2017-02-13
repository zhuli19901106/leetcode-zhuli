// Pure brute-force will result in TLE.
// You can use the same idea, but do it fast with rolling hash.
// Let's suppose no collision here, 
// otherwise there should be an extra price in double-checking.
// The code can look a bit complicated though.

// The idea is from @buyijie
// https://discuss.leetcode.com/topic/73603/c-o-n-2-solution-using-string-hashing

// Actually, the idea of rolling hash can be combined with trie to make it even more efficient.
// But the code would be too damn twisty, you don't wanna try it in an interview.
#include <cstdint>
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> res;
        vector<int> p(2);
        
        auto &a = words;
        int na = a.size();
        
        // Forward hash key
        vector<vector<int64_t>> h;
        // Reverse hash key
        vector<vector<int64_t>> rh;
        h.resize(na);
        rh.resize(na);
        pw.resize(1, 1);
        
        int i;
        for (i = 0; i < na; ++i) {
            calcHash(a[i], h[i], rh[i]);
        }
        
        bool match;
        int n1, n2;
        int j;
        for (i = 0; i < na; ++i) {
            for (j = 0; j < na; ++j) {
                if (i == j) {
                    continue;
                }
                
                n1 = a[i].size();
                n2 = a[j].size();
                match = false;
                
                if (n1 < n2) {
                    if (hash(h[i], 1, n1) == rhash(rh[j], n2 - n1 + 1, n2) && 
                        hash(h[j], 1, n2 - n1) == 
                        rhash(rh[j], 1, n2 - n1)) {
                        match = true;
                    }
                } else if (n1 > n2) {
                    if (hash(h[i], 1, n2) == rhash(rh[j], 1, n2) && 
                        hash(h[i], n2 + 1, n1) == 
                        rhash(rh[i], n2 + 1, n1)) {
                        match = true;
                    }
                } else {
                    if (hash(h[i], 1, n1) == rhash(rh[j], 1, n2)) {
                        match = true;
                    }
                }
                
                if (match) {
                    p[0] = i;
                    p[1] = j;
                    res.push_back(p);
                }
            }
        }
        
        h.clear();
        rh.clear();
        pw.clear();
        
        return res;
    }
private:
    // Prime number used for hash calculation
    static const int64_t P = 37;
    vector<int64_t> pw;
    
    void calcHash(const string &s, vector<int64_t> &h, vector<int64_t> &rh) {
        int ls = s.size();
        h.resize(ls + 2, 0);
        rh.resize(ls + 2, 0);
        int i;
        
        for (i = 1; i <= ls; ++i) {
            h[i] = h[i - 1] * P + (s[i - 1] - 'a' + 1);
        }
        for (i = ls; i >= 1; --i) {
            rh[i] = rh[i + 1] * P + (s[i - 1] - 'a' + 1);
        }
    }
    
    int64_t hash(vector<int64_t> &h, int left, int right) {
        // Parameter check omitted here
        return h[right] - h[left - 1] * getPow(right - left + 1);
    }
    
    int64_t rhash(vector<int64_t> &rh, int left, int right) {
        // Parameter check omitted here
        return rh[left] - rh[right + 1] * getPow(right - left + 1);
    }
    
    int64_t getPow(int i) {
        while (pw.size() <= i) {
            pw.push_back(pw.back() * P);
        }
        return pw[i];
    }
};
