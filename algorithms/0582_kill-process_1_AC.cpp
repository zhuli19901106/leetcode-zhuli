#include <unordered_map>
#include <vector>
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        unordered_map<int, int> dj;
        int n = pid.size();
        int i;
        for (i = 0; i < n; ++i) {
            if (ppid[i] != 0) {
                dj[pid[i]] = ppid[i];
            } else {
                dj[pid[i]] = pid[i];
            }
        }
        dj[kill] = kill;
        
        vector<int> res;
        for (auto &p: dj) {
            if (findRoot(dj, p.first) == kill) {
                res.push_back(p.first);
            }
        }
        sort(res.begin(), res.end());
        dj.clear();
        
        return res;
    }
private:
    int findRoot(unordered_map<int, int> &dj, int x) {
        int r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        int k = x;
        while (x != dj[x]) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
