class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int n = data.size();
        int i;
        int j;
        int k;
        
        for (i = 0; i < n; ++i) {
            data[i] &= 0xff;
        }
        
        i = 0;
        while (i < n) {
            if ((data[i] & 0x80) == 0) {
                ++i;
                continue;
            }
            for (j = 2; j <= 4; ++j) {
                if (!leadingOnes(data[i], j)) {
                    continue;
                }
                for (k = 1; k < j; ++k) {
                    if (i + k >= n || !leadingOnes(data[i + k], 1)) {
                        return false;
                    }
                }
                break;
            }
            if (j > 4) {
                return false;
            }
            i += j;
        }
        return true;
    }
private:
    inline bool leadingOnes(int data, int cnt) {
        return (data >> 7 - cnt) == ((1 << cnt) - 1 << 1);
    }
};
