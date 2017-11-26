#include <string>
#include <vector>
using std::to_string;
using std::vector;

class Solution {
public:
    int compress(vector<char>& chars) {
        auto &a = chars;
        int n = a.size();
        int i, j;
        int k = 0;
        string sd;
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && a[i] == a[j]) {
                ++j;
            }
            if (j - i == 1) {
                a[k++] = a[i];
            } else {
                a[k++] = a[i];
                sd = to_string(j - i);
                for (char &c: sd) {
                    a[k++] = c;
                }
            }
            i = j;
        }
        return k;
    }
};
