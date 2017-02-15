// Brute-force
#include <algorithm>
using std::min;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size() + nums2.size();
        double res = 0;
        res += kthSmallest(nums1, nums2, n - 1 >> 1);
        res += kthSmallest(nums1, nums2, n >> 1);
        res /= 2.0;
        
        return res;
    }
private:
    int kthSmallest(vector<int> &v1, vector<int> &v2, int k) {
        int n1 = v1.size();
        int n2 = v2.size();
        int i1 = 0;
        int i2 = 0;
        int i;
        for (i = 0; i < k; ++i) {
            if (i1 == n1) {
                ++i2;
            } else if (i2 == n2) {
                ++i1;
            } else if (v1[i1] < v2[i2]) {
                ++i1;
            } else {
                ++i2;
            }
        }
        if (i1 == n1) {
            return v2[i2];
        } else if (i2 == n2) {
            return v1[i1];
        } else {
            return min(v1[i1], v2[i2]);
        }
    }
};
