/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::unordered_map;
using std::unordered_set;
using std::vector;

typedef UndirectedGraphNode UGN;

class Solution {
public:
    UGN *cloneGraph(UGN *node) {
        if (node == NULL) {
            return NULL;
        }
        unordered_map<UGN *, int> indices;
        vector<UGN *> nodes;
        unordered_set<UGN *> visited;
        dfs(node, indices, nodes, visited);
        
        UGN *new_node = nodes[0];
        indices.clear();
        nodes.clear();
        visited.clear();
        
        return new_node;
    }
private:
    void dfs(UGN *node, unordered_map<UGN *, int> &indices, 
        vector<UGN *> &nodes, unordered_set<UGN *> &visited) {
        if (visited.find(node) != visited.end()) {
            return;
        } else {
            visited.insert(node);
        }
        
        int idx = nodes.size();
        indices[node] = idx;
        nodes.push_back(new UGN(node->label));
        
        UGN *node1;
        int i;
        int nc = node->neighbors.size();
        for (i = 0; i < nc; ++i) {
            node1 = node->neighbors[i];
            dfs(node1, indices, nodes, visited);
        }
        for (i = 0; i < nc; ++i) {
            node1 = node->neighbors[i];
            nodes[idx]->neighbors.push_back(nodes[indices[node1]]);
        }
    }
};
