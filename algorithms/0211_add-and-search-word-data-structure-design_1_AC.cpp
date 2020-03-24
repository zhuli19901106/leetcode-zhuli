// 1AC
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
        // Be defensive with destructors
        int len = child.size();
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


class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        int lw = word.size();
        if (lw == 0) {
            return;
        }
        
        int i;
        int idx;
        TrieNode *p1;
        
        p1 = root;
        for (i = 0; i < lw; ++i) {
            idx = word[i] - 'a';
            if (p1->child[idx] == NULL) {
                p1->child[idx] = new TrieNode(word[i], p1);
            }
            p1 = p1->child[idx];
        }
        p1->is_word = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return dfs(0, root, word);
    }
    
    ~WordDictionary() {
        delete root;
        root = NULL;
    }
private:
    TrieNode *root;
    
    bool dfs(int idx, TrieNode *root, string &s) {
        while (idx < s.size() && s[idx] != '.') {
            root = root->child[s[idx] - 'a'];
            if (root == NULL) {
                return false;
            }
            ++idx;
        }
        if (idx == s.size()) {
            return root->is_word;
        }
        
        int i;
        for (i = 0; i < root->child.size(); ++i) {
            if (root->child[i] != NULL && dfs(idx + 1, root->child[i], s)) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */
