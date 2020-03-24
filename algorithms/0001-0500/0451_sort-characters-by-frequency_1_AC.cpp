#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>
using std::make_pair;
using std::pair;
using std::sort;
using std::unordered_map;
using std::vector;

typedef pair<char, int> PCI;
typedef unordered_map<char, int> UMCI;

bool comparator(const PCI &p1, const PCI &p2)
{
    if (p1.second != p2.second) {
        return p1.second > p2.second;
    }
    if (p1.first != p2.first) {
        return p1.first < p2.first;
    }
    return true;
}

class Solution {
public:
    string frequencySort(string s) {
        UMCI um;
        int n = s.size();
        int i;
        for (i = 0; i < n; ++i) {
            ++um[s[i]];
        }
        
        UMCI::iterator it;
        vector<PCI> v;
        for (it = um.begin(); it != um.end(); ++it) {
            v.push_back(make_pair(it->first, it->second));
        }
        um.clear();
        sort(v.begin(), v.end(), comparator);
        
        string res = "";
        int j;
        n = v.size();
        for (i = 0; i < n; ++i) {
            for (j = 0; j < v[i].second; ++j) {
                res.push_back(v[i].first);
            }
        }
        v.clear();
        
        return res;
    }
};
