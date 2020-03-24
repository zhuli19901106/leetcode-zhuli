#include <algorithm>
#include <cstdint>
#include <unordered_map>
#include <vector>
using std::sort;
using std::unordered_map;
using std::vector;

class Solution {
public:
    bool isReflected(vector<pair<int, int>>& points) {
        unordered_map<int, vector<int>> um;
        auto &a = points;
        int n = a.size();
        int i;
        for (i = 0; i < n; ++i) {
            um[a[i].second].push_back(a[i].first);
        }
        
        bool res = true;
        bool first_run = true;
        bool sym;
        int64_t x, x1;
        for (auto it = um.begin(); it != um.end(); ++it) {
            sort(it->second.begin(), it->second.end());
            deduplicate(it->second);
            if (first_run) {
                first_run = false;
                sym = isSymmetric(it->second, x);
            } else {
                sym = isSymmetric(it->second, x1);
                if (x != x1) {
                    res = false;
                    break;
                }
            }
            if (!sym) {
                res = false;
                break;
            }
        }
        um.clear();
        
        return res;
    }
private:
    void deduplicate(vector<int> &v) {
        int n = v.size();
        int i, j, k;
        i = k = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && v[j] == v[i]) {
                ++j;
            }
            v[k++] = v[i];
            i = j;
        }
        v.resize(k);
    }
    
    bool isSymmetric(vector<int> &v, int64_t &x) {
        int n = v.size();
        if (n == 0) {
            return false;
        }
        x = 0LL + v[(n - 1) / 2] + v[n / 2];
        
        int i = 0;
        int j = n - 1;
        while (i <= j) {
            if (v[i] + v[j] != x) {
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }
};
