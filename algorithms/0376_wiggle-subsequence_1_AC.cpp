class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        compress(nums);
        int n = nums.size();
        if (n <= 2) {
            return n;
        }
        
        int res = 2;
        int i;
        for (i = 1; i < n -1; ++i) {
            if (nums[i] < nums[i - 1] && nums[i] < nums[i + 1]) {
                ++res;
            } else if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                ++res;
            }
        }
        return res;
    }
private:
    void compress(vector<int> &nums) {
        int n = nums.size();
        int i, j, k;
        
        i = 0;
        k = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && nums[j] == nums[i]) {
                ++j;
            }
            nums[k++] = nums[i++];
            i = j;
        }
        nums.resize(k);
    }
};
