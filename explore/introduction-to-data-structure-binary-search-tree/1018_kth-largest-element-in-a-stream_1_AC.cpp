#include <queue>
#include <vector>
using std::priority_queue;
using std::vector;

class KthLargest {
public:
    KthLargest(int k, vector<int> nums) {
        this->K = k;

        int n = nums.size();
        if (nums.empty()) {
            return;
        }
        int i;
        for (i = 0; i < n; ++i) {
            if (i < k) {
                pq.push(nums[i]);
            }
        }
        for (i = k; i < n; ++i) {
            if (pq.top() < nums[i]) {
                pq.pop();
                pq.push(nums[i]);
            }
        }
    }

    int add(int val) {
        if (pq.size() < this->K) {
            pq.push(val);
        } else if (pq.top() < val) {
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
private:
    priority_queue<int, vector<int>, greater<int>> pq;
    
    int K;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
