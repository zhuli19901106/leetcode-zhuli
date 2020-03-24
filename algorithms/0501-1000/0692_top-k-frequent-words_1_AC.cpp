#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using std::pair;
using std::sort;
using std::string;
using std::unordered_map;
using std::vector;

typedef pair<string, int> PSI;
bool comparator(const PSI &p1, const PSI &p2)
{
    if (p1.second != p2.second) {
        return p1.second > p2.second;
    } else {
        return p1.first < p2.first;
    }
}

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> um;
        for (auto &w: words) {
            ++um[w];
        }
        
        vector<PSI> vp;
        for (auto &p: um) {
            vp.push_back(p);
        }
        sort(vp.begin(), vp.end(), comparator);
        
        vector<string> res;
        int ki = 0;
        for (auto &p: vp) {
            res.push_back(p.first);
            ++ki;
            if (ki >= k) {
                break;
            }
        }
        return res;
    }
};
