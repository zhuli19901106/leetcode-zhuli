#include <algorithm>
using std::max;
using std::min;
using std::swap;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, nums.size() - k);
    }
    
    int quickSelect(vector<int> &nums, int k) {
        k = max(k, 0);
        k = min(k, (int)nums.size() - 1);
        return qSelect(nums, 0, nums.size() - 1, k);
    }
private:
    int qSelect(vector<int> &nums, int left, int right, int k) {
        if (left == right) {
            return nums[left];
        }
        int pivot = nums[left];
        int i = left + 1;
        int j = right;
        while (true) {
            while (i <= j && nums[i] <= pivot) {
                ++i;
            }
            while (i <= j && nums[j] >= pivot) {
                --j;
            }
            if (i > j) {
                break;
            }
            swap(nums[i++], nums[j--]);
        }
        swap(nums[left], nums[j]);
        if (k < j) {
            return qSelect(nums, left, j - 1, k);
        } else if (k > j) {
            return qSelect(nums, j + 1, right, k);
        } else {
            return nums[j];
        }
    }
};
