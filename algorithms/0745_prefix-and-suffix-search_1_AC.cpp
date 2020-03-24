// I'm disappointed to see the problems on Leetcode are becoming more an more tedious.
// It's supposed to be brainy, not unnerving.
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::reverse;
using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

typedef unordered_set<int> USIT;
static const int N = 26;
struct Trie {
	bool is_word;
	USIT idx;
	vector<Trie *> child;
	
	Trie() {
		is_word = false;
		child.resize(N, NULL);
	}
	
	~Trie() {
		idx.clear();
		int i;
		for (i = 0; i < N; ++i) {
			if (child[i] != NULL) {
				delete child[i];
				child[i] = NULL;
			}
		}
		child.clear();
	}
};

class WordFilter {
public:
    WordFilter(vector<string> words) {
		r1 = new Trie();
		r2 = new Trie();
		
		unordered_map<string, int> um;
		int n = words.size();
		int i;
		for (i = 0; i < n; ++i) {
			um[words[i]] = i;
		}
		for (auto &p: um) {
			insert(p.first, p.second);
		}
		um.clear();
    }
    
    int f(string prefix, string suffix) {
		Trie *p1 = find(r1, prefix);
		reverse(suffix.begin(), suffix.end());
		Trie *p2 = find(r2, suffix);
		if (p1 == NULL || p2 == NULL) {
			return -1;
		}
		return maxIntersect(p1->idx, p2->idx);
    }
	
	~WordFilter() {
		delete r1;
		r1 = NULL;
		delete r2;
		r2 = NULL;
	}
private:
	Trie *r1, *r2;
	
	void insert(string s, int idx) {
		int ls = s.size();
		if (ls == 0) {
			return;
		}
		
		string s1 = s;
		string s2 = s;
		reverse(s2.begin(), s2.end());
		
		insert(r1, s1, idx);
		insert(r2, s2, idx);
	}
	
	void insert(Trie *root, string s, int idx) {
		int ls = s.size();
		if (ls == 0) {
			return;
		}
		
		Trie *ptr = root;
		int i, j;
		for (i = 0; i < ls; ++i) {
			ptr->idx.insert(idx);
			j = s[i] - 'a';
			if (ptr->child[j] == NULL) {
				ptr->child[j] = new Trie();
			}
			ptr = ptr->child[j];
		}
		ptr->idx.insert(idx);
		ptr->is_word = true;
	}
	
	int maxIntersect(const USIT &a, const USIT &b) {
		if (a.size() > b.size()) {
			return maxIntersect(b, a);
		}
		
		// -1 for not found
		int res = -1;
		for (auto &i: a) {
			if (b.find(i) == b.end()) {
				continue;
			}
			if (res == -1 || res < i) {
				res = i;
			}
		}
		return res;
	}
	
	Trie *find(Trie *root, string s) {
		Trie *ptr = root;
		int ls = s.size();
		int i, j;
		for (i = 0; i < ls; ++i) {
			if (ptr == NULL) {
				break;
			}
			j = s[i] - 'a';
			ptr = ptr->child[j];
		}
		return ptr;
	}
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */
