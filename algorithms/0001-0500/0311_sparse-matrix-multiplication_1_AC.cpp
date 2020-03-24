// Hard labor
#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> c;
        int ra = A.size();
        int rb = B.size();
        if (ra == 0 || rb == 0) {
            return c;
        }
        int ca = A[0].size();
        int cb = B[0].size();
        if (ca != rb) {
            return c;
        }
        
        unordered_map<int, unordered_map<int, int>> ma, mb, mc;
        convert(A, ma);
        convert(B, mb);
        
        int x, y, z;
        int v1, v2;
        for (auto it1 = ma.begin(); it1 != ma.end(); ++it1) {
            x = it1->first;
            for (auto it2 = it1->second.begin(); it2 != it1->second.end(); ++it2) {
                y = it2->first;
                v1 = it2->second;
                if (mb.find(y) == mb.end()) {
                    continue;
                }
                for (auto it3 = mb[y].begin(); it3 != mb[y].end(); ++it3) {
                    z = it3->first;
                    v2 = it3->second;
                    mc[x][z] += v1 * v2;
                }
            }
        }
        
        for (auto it1 = mc.begin(); it1 != mc.end(); ++it1) {
            auto it2 = it1->second.begin();
            while (it2 != it1->second.end()) {
                if (it2->second != 0) {
                    ++it2;
                } else {
                    it2 = it1->second.erase(it2);
                }
            }
        }
        
        c.resize(ra, vector<int>(cb, 0));
        for (auto it1 = mc.begin(); it1 != mc.end(); ++it1) {
            for (auto it2 = it1->second.begin(); it2 != it1->second.end(); ++it2) {
                c[it1->first][it2->first] = it2->second;
            }
        }
        
        ma.clear();
        mb.clear();
        mc.clear();
        
        return c;
    }
private:
    void convert(vector<vector<int>> &v, unordered_map<int, unordered_map<int, int>> &um) {
        int n = v.size();
        int m = (n > 0 ? v[0].size() : 0);
        if (n == 0 || m == 0) {
            return;
        }
        int i, j;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (v[i][j] == 0) {
                    continue;
                }
                um[i][j] = v[i][j];
            }
        }
    }
};
