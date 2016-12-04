#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        if (n1 > n2) {
            return intersection(nums2, nums1);
        }
        
        vector<int> res;
        unordered_set<int> s1, s2;
        int i;
        for (i = 0; i < n1; ++i) {
            s1.insert(nums1[i]);
        }
        for (i = 0; i < n2; ++i) {
            s2.insert(nums2[i]);
        }
        unordered_set<int>::const_iterator it;
        for (it = s1.begin(); it != s1.end(); ++it) {
            if (s2.find(*it) != s2.end()) {
                res.push_back(*it);
            }
        }
        s1.clear();
        s2.clear();
        return res;
    }
};
