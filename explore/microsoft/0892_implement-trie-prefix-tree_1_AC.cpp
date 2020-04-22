#include <vector>
using std::vector;

static const int DICT_SIZE = 26;

typedef struct TrieNode {
    TrieNode(char ch = '\0', struct TrieNode *parent = NULL) {
        this->is_word = false;
        this->ch = ch;
        this->child.resize(DICT_SIZE, NULL);
        this->parent = parent;
    }
    
    void clear() {
        int i;
        int len = child.size();
        // Be defensive with destructors
        for (i = 0; i < len; ++i) {
            if (child[i] != NULL) {
                child[i]->clear();
            }
            delete child[i];
            child[i] = NULL;
        }
        child.clear();
    }
    
    ~TrieNode() {
        clear();
    }
    
    bool is_word;
    char ch;
    vector<struct TrieNode *> child;
    struct TrieNode *parent;
} TrieNode;

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *p = root;
        int lw = word.size();
        int i;
        int idx;
        for (i = 0; i < lw; ++i) {
            idx = word[i] - 'a';
            if (p->child[idx] == NULL) {
                p->child[idx] = new TrieNode(word[i], p);
            }
            p = p->child[idx];
        }
        p->is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode *p = root;
        int lw = word.size();
        int i;
        int idx;
        for (i = 0; i < lw; ++i) {
            idx = word[i] - 'a';
            p = p->child[idx];
            if (p == NULL) {
                return false;
            }
        }
        return p->is_word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode *p = root;
        int lp = prefix.size();
        int i;
        int idx;
        for (i = 0; i < lp; ++i) {
            idx = prefix[i] - 'a';
            p = p->child[idx];
            if (p == NULL) {
                return false;
            }
        }
        return p != NULL;
    }
    
    ~Trie() {
        delete root;
        root = NULL;
    }
private:
    TrieNode *root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
