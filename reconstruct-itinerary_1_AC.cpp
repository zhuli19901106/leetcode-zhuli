// Watch out, multigraph!
#include <map>
#include <unordered_map>
using std::map;
using std::unordered_map;

class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        int ne = tickets.size();
        int i;
        string s1, s2;
        for (i = 0; i < ne; ++i) {
            s1 = tickets[i].first;
            s2 = tickets[i].second;
            ++graph[s1][s2];
        }
        
        vector<string> res;
        string start = "JFK";
        
        path.push_back(start);
        bool found = dfs(start, ne, res);
        
        graph.clear();
        path.clear();
        return res;
    }
private:
    unordered_map<string, map<string, int>> graph;
    vector<string> path;
    
    bool dfs(string s, int ec, vector<string> &res) {
        if (ec == 0) {
            res = path;
            return true;
        }
        
        string s1;
        for (auto it = graph[s].begin(); it != graph[s].end(); ++it) {
            if (it->second == 0) {
                // Already checked
                continue;
            }
            s1 = it->first;
            
            --it->second;
            path.push_back(s1);
            if (dfs(s1, ec - 1, res)) {
                return true;
            }
            path.pop_back();
            ++it->second;
        }
        return false;
    }
};
