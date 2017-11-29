#include <vector>
using std::vector;

struct Trie {
public:
    static const int N = 26;
    
    bool is_word;
    int val;
    vector<Trie *> child;
    
    Trie() {
        is_word = false;
        val = 0;
        child.resize(N, NULL);
    }
    
    ~Trie() {
        int i;
        for (i = 0; i < N; ++i) {
            if (child[i] != NULL) {
                delete child[i];
                child[i] = NULL;
            }
        }
    }
};

class MapSum {
public:
    /** Initialize your data structure here. */
    MapSum() {
        root = new Trie();
    }
    
    void insert(string key, int val) {
        int lk = key.size();
        if (lk == 0) {
            return;
        }
        
        Trie *p = root;
        int i, j;
        for (i = 0; i < lk; ++i) {
            j = key[i] - 'a';
            if (p->child[j] == NULL) {
                p->child[j] = new Trie();
            }
            p = p->child[j];
        }
        p->is_word = true;
        p->val = val;
    }
    
    int sum(string prefix) {
        int lp = prefix.size();
        Trie *p = root;
        int i, j;
        for (i = 0; i < lp; ++i) {
            j = prefix[i] - 'a';
            if (p->child[j] == NULL) {
                return 0;
            }
            p = p->child[j];
        }
        return sum(p);
    }
    
    ~MapSum() {
        delete root;
        root = NULL;
    }
private:
    Trie *root;
    
    int sum(Trie *p) {
        if (p == NULL) {
            return 0;
        }
        int res = (p->is_word ? p->val : 0);
        int i;
        for (i = 0; i < Trie::N; ++i) {
            res += sum(p->child[i]);
        }
        return res;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
