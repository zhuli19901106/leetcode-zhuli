// This problem is poorly defined.
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::string;
using std::to_string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class ValidWordAbbr {
public:
    ValidWordAbbr(vector<string> dictionary) {
        auto &a = dictionary;
        for (auto &s: a) {
            if (us.find(s) != us.end()) {
                continue;
            }
            us.insert(s);
            ++um[abbr(s)];
        }
    }
    
    bool isUnique(string word) {
        string t = abbr(word);
        return (us.find(word) != us.end() ? um[t] == 1 : um.find(t) == um.end());
    }
    
    ~ValidWordAbbr() {
        us.clear();
        um.clear();
    }
private:
    unordered_set<string> us;
    unordered_map<string, int> um;
    
    string abbr(string s) {
        int ls = s.size();
        if (ls < 3) {
            return s;
        }
        string t = "";
        t.push_back(s[0]);
        t += to_string(ls - 2);
        t.push_back(s[ls - 1]);
        
        return t;
    }
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj.isUnique(word);
 */
