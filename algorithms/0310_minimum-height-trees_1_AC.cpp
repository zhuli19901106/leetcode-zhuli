// Standard DFS
#include <algorithm>
#include <climits>
#include <unordered_map>
#include <unordered_set>
using std::fill;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int> res;
        if (n == 0) {
            return res;
        }
        
        unordered_map<int, unordered_set<int>> gragh;
        int ne = edges.size();
        int i;
        for (i = 0; i < ne; ++i) {
            gragh[edges[i].first].insert(edges[i].second);
            gragh[edges[i].second].insert(edges[i].first);
        }
        
        vector<int> pre(n);
        vector<int> dist(n);
        vector<bool> visited(n);
        int mi;
        int max_len;
        
        pre[0] = 0;
        fill(dist.begin(), dist.end(), INT_MAX);
        fill(visited.begin(), visited.end(), false);
        traverse(0, 0, pre, gragh, dist, visited);
        
        mi = 0;
        for (i = 1; i < n; ++i) {
            if (dist[i] > dist[mi]) {
                mi = i;
            }
        }
        max_len = dist[mi];
        
        pre[mi] = mi;
        fill(dist.begin(), dist.end(), INT_MAX);
        fill(visited.begin(), visited.end(), false);
        traverse(mi, 0, pre, gragh, dist, visited);
        
        mi = 0;
        for (i = 1; i < n; ++i) {
            if (dist[i] > dist[mi]) {
                mi = i;
            }
        }
        max_len = dist[mi];
        
        fill(visited.begin(), visited.end(), false);
        for (i = 0; i < n; ++i) {
            if (dist[i] == max_len) {
                recoverPath(i, pre, visited);
            }
        }
        for (i = 0; i < n; ++i) {
            if (visited[i]) {
                res.push_back(i);
            }
        }
        
        gragh.clear();
        dist.clear();
        visited.clear();
        return res;
    }
private:
    void traverse(int idx, int len, vector<int> &pre, 
        unordered_map<int, unordered_set<int>> &gragh, vector<int> &dist, 
        vector<bool> &visited) {
        dist[idx] = len;
        visited[idx] = true;
        
        int x;
        for (auto it = gragh[idx].begin(); it != gragh[idx].end(); ++it) {
            x = *it;
            if (visited[x]) {
                continue;
            }
            pre[x] = idx;
            traverse(x, len + 1, pre, gragh, dist, visited);
        }
    }
    
    void recoverPath(int idx, vector<int> &pre, vector<bool> &mark) {
        vector<int> path;
        while (true) {
            path.push_back(idx);
            if (idx == pre[idx]) {
                break;
            }
            idx = pre[idx];
        }
        int max_len = path.size();
        mark[path[path.size() / 2]] = true;
        if ((max_len & 1) == 0) {
            mark[path[path.size() / 2 - 1]] = true;
        }
        path.clear();
    }
};
