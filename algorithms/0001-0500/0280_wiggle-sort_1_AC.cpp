#include <vector>
using std::vector;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        auto &v = nums;
        int n = v.size();
        if (n < 2) {
            return;
        }
        
        int pivot = quickSelect(v, n / 2);
        int i = 0;
        int j = 1;
        int i1 = (n % 2 != 0 ? n - 1 : n - 2);
        int j1 = (n % 2 != 0 ? n - 2 : n - 1);
        while (i < n && j < n) {
            if (v[i] < pivot) {
                i += 2;
                continue;
            }
            if (v[j] > pivot) {
                j += 2;
                continue;
            }
            if (v[i] == pivot && i < i1) {
                swap(v[i], v[i1]);
                i1 -= 2;
                continue;
            }
            if (v[j] == pivot && j < j1) {
                swap(v[j], v[j1]);
                j1 -= 2;
                continue;
            }
            swap(v[i], v[j]);
            i += 2;
            j += 2;
        }
    }
private:
    int quickSelect(vector<int> &v, int k) {
        int n = v.size();
        int pivot;
        int ll, rr;
        int i, j;
        
        ll = 0;
        rr = n - 1;
        while (true) {
            pivot = v[ll];
            if (ll == rr) {
                return pivot;
            }
            i = ll + 1;
            j = rr;
            while (true) {
                while (i <= j && v[i] <= pivot) {
                    ++i;
                }
                while (i <= j && v[j] >= pivot) {
                    --j;
                }
                if (i <= j) {
                    swap(v[i++], v[j--]);
                } else {
                    break;
                }
            }
            swap(v[ll], v[j]);
            
            if (k < j) {
                rr = j - 1;
            } else if (k > j) {
                ll = j + 1;
            } else {
                return v[j];
            }
        }
    }
};
