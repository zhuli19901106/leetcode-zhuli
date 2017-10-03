#include <algorithm>
#include <queue>
#include <vector>
using std::priority_queue;
using std::reverse;
using std::vector;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> res;
        if (k <= 0) {
            return res;
        }
        
        priority_queue<int, vector<int>, greater<int>> pq1;
        priority_queue<int, vector<int>, less<int>> pq2;
        
        int i;
        for (i = 0; i < k; ++i) {
            if (arr[i] >= x) {
                pq2.push(arr[i]);
            } else {
                pq1.push(arr[i]);
            }
        }
        
        int n = arr.size();
        for (i = k; i < n; ++i) {
            if (arr[i] >= x) {
                pq2.push(arr[i]);
            } else {
                pq1.push(arr[i]);
            }
            if (pq1.empty()) {
                pq2.pop();
            } else if (pq2.empty()) {
                pq1.pop();
            } else if (x - pq1.top() > pq2.top() - x) {
                pq1.pop();
            } else {
                pq2.pop();
            }
        }
        
        int n1 = pq1.size();
        while (!pq1.empty()) {
            res.push_back(pq1.top());
            pq1.pop();
        }
        while (!pq2.empty()) {
            res.push_back(pq2.top());
            pq2.pop();
        }
        reverse(res.begin() + n1, res.end());
        
        return res;
    }
};
