// Upper bound
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0 || nums[n - 1] < target) {
            return n;
        }
        if (nums[0] >= target) {
            return 0;
        }
        int ll = 0;
        int rr = n - 1;
        int mm;
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            if (nums[mm] < target) {
                ll = mm;
            } else {
                rr = mm;
            }
        }
        return rr;
    }
};
