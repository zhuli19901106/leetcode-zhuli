// Binary search
// If things got complicated, you're in the wrong way.
#include <algorithm>
#include <vector>
using std::lower_bound;
using std::max;
using std::min;
using std::vector;

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
    
    int kthSmallest(vector<int> &v1, vector<int> &v2, int k) {
        int n1 = v1.size();
        int n2 = v2.size();
        
        return kthSmallestSearch(v1, v2, 0, n1 - 1, 0, n2 - 1, k);
    }
    
    int kthSmallestSearch(vector<int> &v1, vector<int> &v2, int l1, int r1, int l2, int r2, int k) {
        if (l1 > r1) {
            return v2[l2 + k];
        }
        if (l2 > r2) {
            return v1[l1 + k];
        }
        if (l1 == r1) {
            if (l2 == r2) {
                return k == 0 ? min(v1[l1], v2[l2]) : max(v1[l1], v2[l2]);
            } else {
                return kthSmallestSearch(v2, v1, l2, r2, l1, r1, k);
            }
        }
        
        int p1 = l1 + (r1 - l1 >> 1);
        int val = v1[p1];
        int p2 = lower_bound(v2.begin() + l2, v2.begin() + r2 + 1, val) - v2.begin() - 1;
        int cnt = (p1 - l1 + 1) + (p2 - l2 + 1);
        
        // This can be changed to iterative form, but don't wanna bother.
        if (k >= cnt) {
            return kthSmallestSearch(v1, v2, p1 + 1, r1, p2 + 1, r2, k - cnt);
        } else {
            return kthSmallestSearch(v1, v2, l1, p1, l2, p2, k);
        }
    }
};
