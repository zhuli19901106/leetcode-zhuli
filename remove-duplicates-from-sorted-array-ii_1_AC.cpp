class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i, j, k;
        
        i = 0;
        k = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && nums[i] == nums[j]) {
                ++j;
            }
            nums[k++] = nums[i];
            if (j - i >= 2) {
                nums[k++] = nums[i];
            }
            i = j;
        }
        return k;
    }
};
