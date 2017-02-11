// The idea is simple, but the coding can be tricky.
#include <algorithm>
#include <map>
using std::map;
using std::min;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> res;
        int n = nums.size();
        if (n == 0) {
            return res;
        }
        k = min(k, n);
        
        map<int, int> m1;
        map<int, int> m2;
        int c1 = 0;
        int c2 = 0;
        
        int i = 0;
        while (i < k) {
            // Insert nums[i]
            insert(m1, c1, nums[i]);
            balance(m1, c1, m2, c2);
            
            ++i;
        }
        
        double val;
        while (true) {
            if (c1 == c2) {
                val = (1.0 * m1.rbegin()->first + m2.begin()->first) / 2.0;
            } else {
                val = m1.rbegin()->first;
            }
            res.push_back(val);
            
            if (i >= n) {
                break;
            }
            
            // Remove nums[i - k]
            if (m1.find(nums[i - k]) != m1.end()) {
                remove(m1, c1, nums[i - k]);
            } else {
                remove(m2, c2, nums[i - k]);
            }
            
            // Insert nums[i]
            insert(m1, c1, nums[i]);
            balance(m1, c1, m2, c2);
            
            ++i;
        }
        m1.clear();
        c1 = 0;
        m2.clear();
        c2 = 0;
        
        return res;
    }
private:
    void insert(map<int, int> &mm, int &cnt, int val) {
        ++mm[val];
        ++cnt;
    }

    void remove(map<int, int> &mm, int &cnt, int val) {
        if (mm.find(val) == mm.end()) {
            return;
        }
        --mm[val];
        if (mm[val] == 0) {
            mm.erase(val);
        }
        --cnt;
    }
    
    void balance(map<int, int> &m1, int &c1, map<int, int> &m2, int &c2) {
        int n1, n2;
        
        while (c1 < c2) {
            n2 = m2.begin()->first;
            remove(m2, c2, n2);
            insert(m1, c1, n2);
        }
        
        while (c1 > c2 + 1) {
            n1 = m1.rbegin()->first;
            remove(m1, c1, n1);
            insert(m2, c2, n1);
        }
        
        while (c2 > 0) {
            n1 = m1.rbegin()->first;
            n2 = m2.begin()->first;
            if (n1 <= n2) {
                break;
            }
            remove(m1, c1, n1);
            insert(m1, c1, n2);
            remove(m2, c2, n2);
            insert(m2, c2, n1);
        }
    }
};
