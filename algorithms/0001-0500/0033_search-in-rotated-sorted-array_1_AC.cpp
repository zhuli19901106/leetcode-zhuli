class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) {
            return -1;
        }
        int offset = findPivot(nums);
        int ll, mm, rr;
        
        ll = offset;
        rr = offset + n - 1;
        while (ll <= rr) {
            mm = ll + (rr - ll >> 1);
            if (target < nums[mm % n]) {
                rr = mm - 1;
            } else if (target > nums[mm % n]) {
                ll = mm + 1;
            } else {
                return mm % n;
            }
        }
        return -1;
    }
private:
    int findPivot(vector<int> &nums) {
        int n = nums.size();
        if (n < 2 || nums[0] < nums[n - 1]) {
            return 0;
        }
        int ll, mm, rr;
        
        ll = 0;
        rr = n - 1;
        while (rr - ll > 1) {
            if (nums[ll] == nums[rr]) {
                ++ll;
                continue;
            }
            mm = ll + (rr - ll >> 1);
            if (nums[mm] >= nums[ll]) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return rr;
    }
};
