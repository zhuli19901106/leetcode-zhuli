#include <string>
#include <vector>
using std::string;
using std::vector;

static const int DICT_SIZE = 26;
static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

typedef vector<vector<bool>> VVB;
typedef vector<vector<char>> VVC;
typedef vector<string> VS;

typedef struct TrieNode {
    bool is_word;
    vector<TrieNode *> child;
    
    TrieNode() {
        is_word = false;
        child.resize(DICT_SIZE, NULL);
    }
    
    ~TrieNode() {
        int nc = child.size();
        int i;
        for (i = 0; i < nc; ++i) {
            if (child[i] == NULL) {
                continue;
            }
            delete child[i];
            child[i] = NULL;
        }
        child.clear();
    }
} TrieNode;

class Solution {
public:
    VS findWords(VVC &board, VS &words) {
        VS res;
        if (words.size() == 0) {
            return res;
        }
        
        auto &a = board;
        n = a.size();
        m = n > 0 ? a[0].size() : 0;
        if (n == 0 || m == 0) {
            return res;
        }
        
        TrieNode *root = new TrieNode();
        for (auto &w: words) {
            insertWord(root, w);
        }
        
        int i, j;
        v.resize(n, vector<bool>(m, false));
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                w.push_back(a[i][j]);
                v[i][j] = true;
                
                dfs(i, j, root->child[a[i][j] - 'a'], a, res);
                
                v[i][j] = false;
                w.pop_back();
            }
        }
        v.clear();
        w.clear();
        
        delete root;
        root = NULL;
        
        return res;
    }
private:
    string w;
    VVB v;
    int n, m;
    
    void insertWord(TrieNode *root, const string &s) {
        int ls = s.size();
        if (ls == 0) {
            return;
        }
        
        TrieNode *p = root;
        int i;
        for (i = 0; i < ls; ++i) {
            if (p->child[s[i] - 'a'] == NULL) {
                p->child[s[i] - 'a'] = new TrieNode();
            }
            p = p->child[s[i] - 'a'];
        }
        p->is_word = true;
    }
    
    void dfs(int i, int j, TrieNode *p, VVC &a, VS &res) {
        if (p == NULL) {
            return;
        }
        if (p->is_word) {
            res.push_back(w);
            // Next time you won't stop by.
            p->is_word = false;
        }
        
        int k;
        int i1, j1;
        for (k = 0; k < 4; ++k) {
            i1 = i + offset[k][0];
            j1 = j + offset[k][1];
            if (i1 < 0 || i1 > n - 1 || j1 < 0 || j1 > m - 1) {
                continue;
            }
            if (v[i1][j1]) {
                continue;
            }
            w.push_back(a[i1][j1]);
            v[i1][j1] = true;
            
            dfs(i1, j1, p->child[a[i1][j1] - 'a'], a, res);
            
            v[i1][j1] = false;
            w.pop_back();
        }
    }
};
