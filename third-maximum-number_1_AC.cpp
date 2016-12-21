#include <algorithm>
#include <queue>
#include <unordered_set>
using std::max;
using std::priority_queue;
using std::unordered_set;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        deduplicate(nums);
        
        int n = nums.size();
        int i = 0;
        int res;
        if (n < k) {
            res = nums[0];
            for (i = 1; i < n; ++i) {
                res = max(res, nums[i]);
            }
            return res;
        }
        
        priority_queue<int, vector<int>, greater<int>> pq;
        while (i < k) {
            pq.push(nums[i]);
            ++i;
        }
        while (i < n) {
            if (nums[i] > pq.top()) {
                pq.pop();
                pq.push(nums[i]);
            }
            ++i;
        }
        res = pq.top();
        while (!pq.empty()) {
            pq.pop();
        }
        
        return res;
    }
private:
    static const int k = 3;
    
    void deduplicate(vector<int> &nums) {
        unordered_set<int> us;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            us.insert(nums[i]);
        }
        nums.clear();
        unordered_set<int>::const_iterator it;
        for (it = us.begin(); it != us.end(); ++it) {
            nums.push_back(*it);
        }
        us.clear();
    }
};
