// Union-find set;
#include <unordered_map>
using std::unordered_map;

typedef unordered_map<string, string> UMSS;
typedef unordered_map<string, double> UMSD;

class Solution {
public:
    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) {
        static const double DOUBLE_UNDEF = -1.0;
        
        int n = equations.size();
        int m = queries.size();
        UMSS dj;
        UMSD q;
        string x, y;
        string rx, ry;
        
        int i;
        for (i = 0; i < n; ++i) {
            x = equations[i].first;
            y = equations[i].second;
            if (dj.find(x) == dj.end()) {
                dj[x] = x;
                q[x] = 1.0;
            }
            if (dj.find(y) == dj.end()) {
                dj[y] = y;
                q[y] = 1.0;
            }
            
            rx = findRoot(dj, q, x);
            ry = findRoot(dj, q, y);
            if (rx == ry) {
                // If there's no contradiction, nothing to be done here.
                continue;
            }
            
            dj[rx] = ry;
            // The values are positive here.
            q[rx] = values[i] * q[y] / q[x];
        }
        
        vector<double> res;
        for (i = 0; i < m; ++i) {
            x = queries[i].first;
            y = queries[i].second;
            if (dj.find(x) == dj.end() || dj.find(y) == dj.end()) {
               res.push_back(DOUBLE_UNDEF);
               continue;
            }
            rx = findRoot(dj, q, x);
            ry = findRoot(dj, q, y);
            if (rx != ry) {
                // Disjoint
                res.push_back(DOUBLE_UNDEF);
                continue;
            }
            res.push_back(q[x] / q[y]);
        }
        dj.clear();
        q.clear();
        
        return res;
    }
private:
    string findRoot(UMSS &dj, UMSD &q, string x) {
        string r, k;
        vector<string> path;
        
        r = x;
        while (dj[r] != r) {
            path.push_back(r);
            r = dj[r];
        }
        
        int n = path.size();
        int i;
        double val = 1.0;
        // Path compression
        for (i = n - 1; i >= 0; --i) {
            dj[path[i]] = r;
            val *= q[path[i]];
            q[path[i]] = val;
        }
        return r;
    }
};
