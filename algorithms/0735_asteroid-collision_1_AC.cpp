#include <algorithm>
#include <vector>
using std::reverse;
using std::vector;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        auto &a = asteroids;
        int n = a.size();
        vector<int> res;
        if (n == 0) {
            return res;
        }
        
        vector<int> st;
        int i;
        for (i = 0; i < n; ++i) {
            if (a[i] < 0) {
                while (!st.empty() && a[i] + st.back() < 0) {
                    st.pop_back();
                }
                if (st.empty()) {
                    res.push_back(a[i]);
                    continue;
                }
                if (a[i] + st.back() == 0) {
                    st.pop_back();
                }
            } else {
                st.push_back(a[i]);
            }
        }
        
        reverse(st.begin(), st.end());
        while (!st.empty()) {
            res.push_back(st.back());
            st.pop_back();
        }
        
        return res;
    }
};
