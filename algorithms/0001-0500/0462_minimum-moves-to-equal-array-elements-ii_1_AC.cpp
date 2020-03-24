// Median
// Quick Sort, a permanent bug detector.
#include <algorithm>
#include <cmath>
#include <cstdint>
using std::abs;
using std::max;
using std::min;
using std::sort;
using std::swap;

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int median;
        int64_t res;
        int n = nums.size();
        
        median = quickSelect(nums, n / 2 - 1);
        res = totalDist(nums, median);
        median = quickSelect(nums, (n - 1) / 2);
        res = min(res, totalDist(nums, median));
        return res;
    }
    
    int64_t totalDist(vector<int>& v, int x) {
        int n = v.size();
        int64_t res = 0;
        int i;
        for (i = 0; i < n; ++i) {
            res += abs(v[i] - x);
        }
        return res;
    }
private:
    int quickSelect(vector<int>& v, int k) {
        int n = v.size();
        k = max(k, 0);
        k = min(k, n - 1);
        return qSelect(v, 0, n - 1, k);
    }
    
    int qSelect(vector<int>& v, int left, int right, int k) {
        if (left == right) {
            return v[left];
        }
        int pivot = v[left];
        int i = left + 1;
        int j = right;
        while (true) {
            while (i <= j && v[i] < pivot) {
                ++i;
            }
            while (j >= i && v[j] > pivot) {
                --j;
            }
            if (i > j) {
                break;
            }
            swap(v[i++], v[j--]);
        }
        swap(v[j], v[left]);
        if (k < j) {
            return qSelect(v, left, j - 1, k);
        } else if (k > j) {
            return qSelect(v, j + 1, right, k);
        } else {
            return v[k];
        }
    }
};
