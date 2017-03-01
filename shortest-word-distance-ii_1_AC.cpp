// Straight-forward hashing solution
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <vector>
using std::abs;
using std::min;
using std::string;
using std::unordered_map;
using std::vector;

class WordDistance {
public:
    WordDistance(vector<string> words) {
        auto &a = words;
        int n = a.size();
        int i;
        for (i = 0; i < n; ++i) {
            um[a[i]].push_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        if (cache.find(word1) != cache.end() && cache[word1].find(word2) != 
            cache[word1].end()) {
            return cache[word1][word2];
        }
        auto &v1 = um[word1];
        auto &v2 = um[word2];
        int n1 = v1.size();
        int n2 = v2.size();
        int res = INT_MAX;
        int i, j;
        
        i = j = 0;
        while (i < n1 && j < n2) {
            res = min(res, abs(v1[i] - v2[j]));
            if (v1[i] < v2[j]) {
                ++i;
            } else {
                ++j;
            }
        }
        cache[word1][word2] = cache[word2][word1] = res;
        return res;
    }
    
    ~WordDistance() {
        um.clear();
        cache.clear();
    }
private:
    unordered_map<string, vector<int>> um;
    unordered_map<string, unordered_map<string, int>> cache;
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(words);
 * int param_1 = obj.shortest(word1,word2);
 */
