#include <vector>
using std::vector;

class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> v(n);
        int i = 0;
        v[i++] = 1;
        
        int f = 0;
        int i1 = 2;
        int i2 = n;
        while (k > 1) {
            f = 1 - f;
            if (f) {
                v[i++] = i2--;
            } else {
                v[i++] = i1++;
            }
            --k;
        }
        while (i1 <= i2) {
            if (f) {
                v[i++] = i2--;
            } else {
                v[i++] = i1++;
            }
        }
        return v;
    }
};
