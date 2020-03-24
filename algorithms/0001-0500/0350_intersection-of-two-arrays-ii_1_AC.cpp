#include <algorithm>
#include <unordered_map>
using std::unordered_map;
using std::min;

typedef unordered_map<int, int> UMII;
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        UMII ht1, ht2;
        int i;
        int n1 = nums1.size();
        for (i = 0; i < n1; ++i) {
            ++ht1[nums1[i]];
        }
        int n2 = nums2.size();
        for (i = 0; i < n2; ++i) {
            ++ht2[nums2[i]];
        }
        return mergeResult(ht1, ht2);
    }
private:
    vector<int> mergeResult(UMII& um1, UMII& um2) {
        if (um1.size() > um2.size()) {
            return mergeResult(um2, um1);
        }
        
        vector<int> res;
        UMII::const_iterator it;
        int i;
        int key, val;
        for (it = um1.begin(); it != um1.end(); ++it) {
            key = it->first;
            if (um2.find(key) == um2.end()) {
                continue;
            }
            val = min(um1[key], um2[key]);
            for (i = 0; i < val; ++i) {
                res.push_back(key);
            }
        }
        return res;
    }
};
