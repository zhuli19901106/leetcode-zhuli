// Easy? WTF?
#include <algorithm>
#include <map>
#include <unordered_map>
#include <unordered_set>
using std::map;
using std::min;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n <= 1) {
            return 1;
        }
        
        tf.clear();
        idf.clear();
        for (auto &x: a) {
            tf[x] = 0;
            idf[0].insert(x);
        }
        for (auto &x: a) {
            add(x);
        }
        int max_deg = idf.rbegin()->first;
        
        int res = n;
        int i, j;
        i = j = 0;
        tf.clear();
        idf.clear();
        while (i < n && j < n) {
            while (j < n && idf[max_deg].empty()) {
                add(a[j++]);
            }
            while (i < j && !idf[max_deg].empty()) {
                res = min(res, j - i);
                remove(a[i++]);
            }
        }
        
        return res;
    }
private:
    unordered_map<int, int> tf;
    map<int, unordered_set<int>> idf;
    
    void add(int n) {
        int c = tf[n];
        ++tf[n];
        idf[c].erase(n);
        idf[c + 1].insert(n);
    }
    
    void remove(int n) {
        int c = tf[n];
        if (c == 0) {
            return;
        }
        --tf[n];
        idf[c].erase(n);
        idf[c - 1].insert(n);
    }
};
