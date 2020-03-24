class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int i = n - 1;
        while (i >= 0 && digits[i] == 9) {
            --i;
        }
        if (i < 0) {
            digits.push_back(0);
            digits[0] = 1;
            for (i = 1; i < n; ++i) {
                digits[i] = 0;
            }
        } else {
            ++digits[i];
            while (++i < n) {
                digits[i] = 0;
            }
        }
        return digits;
    }
};
