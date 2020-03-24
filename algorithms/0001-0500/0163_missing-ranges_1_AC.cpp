// So many edge cases, what a headache.
#include <iterator>
#include <map>
#include <string>
#include <vector>
using std::map;
using std::next;
using std::string;
using std::to_string;
using std::vector;

class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        map<int, int> m1, m2;
        
        int n = nums.size();
        int i, j;
        
        i = 0;
        while (i < n) {
            insert(nums[i], m1, m2, lower, upper);
            j = i + 1;
            while (j < n && nums[i] == nums[j]) {
                ++j;
            }
            i = j;
        }
        
        vector<string> res;
        int x, y;
        
        bool check;
        x = lower;
        y = (m1.size() > 0 ? m1.begin()->first - 1 : upper);
        check = (m1.size() == 0 || lower < m1.begin()->first);
        if (check && x <= y) {
            res.push_back(interval(x, y));
        }
        auto it = m1.begin();
        auto next_it = it;
        while (it != m1.end()) {
            next_it = next(it);
            x = it->second + 1;
            y = (next_it != m1.end() ? next_it->first - 1 : upper);
            check = (it->second < y);
            if (check && x <= y) {
                res.push_back(interval(x, y));
            }
            
            it = next_it;
        }
        m1.clear();
        m2.clear();
        
        return res;
    }
private:
    void insert(int i, map<int, int> &m1, map<int, int> &m2, int lower, int upper) {
        int left, right;
        if (i > lower && m2.find(i - 1) != m2.end()) {
            left = m2[i - 1];
            m2.erase(i - 1);
        } else {
            left = i;
        }
        if (i < upper && m1.find(i + 1) != m1.end()) {
            right = m1[i + 1];
            m1.erase(i + 1);
        } else {
            right = i;
        }
        
        m1[left] = right;
        m2[right] = left;
    }
    
    string interval(int x, int y) {
        return (x == y ? to_string(x) : to_string(x) + "->" + to_string(y));
    }
};
