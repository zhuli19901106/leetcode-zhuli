// Enumerate all possible combination.
// The comparison during the string merge can't be done in O(1) time.
#include <algorithm>
#include <string>
#include <vector>
using std::reverse;
using std::string;
using std::vector;

class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<string> v1, v2;
        string s1 = vtos(nums1);
        string s2 = vtos(nums2);
        int ls1 = s1.size();
        int ls2 = s2.size();
        
        string s;
        
        s = s1;
        while (s.size() > 0) {
            v1.push_back(s);
            s = dropOne(s);
        }
        v1.push_back(s);
        reverse(v1.begin(), v1.end());
        
        s = s2;
        while (s.size() > 0) {
            v2.push_back(s);
            s = dropOne(s);
        }
        v2.push_back(s);
        reverse(v2.begin(), v2.end());
        
        string res = "";
        int i;
        for (i = 0; i < k; ++i) {
            res.push_back('0');
        }
        
        int j;
        for (i = 0; i <= k; ++i) {
            j = k - i;
            if (i > ls1 || j > ls2) {
                continue;
            }
            s = mergeTwo(v1[i], v2[j]);
            if (s > res) {
                res = s;
            }
        }
        v1.clear();
        v2.clear();
        
        vector<int> v = stov(res);
        
        return v;
    }
private:
    string vtos(const vector<int> &v) {
        string s = "";
        for (const int &i: v) {
            s.push_back(i + '0');
        }
        return s;
    }
    
    vector<int> stov(const string &s) {
        vector<int> v;
        for (const char &c: s) {
            v.push_back(c - '0');
        }
        return v;
    }
    
    string dropOne(const string &s) {
        int ls = s.size();
        if (ls < 2) {
            return "";
        }
        
        string s1 = "";
        int i;
        for (i = 0; i + 1 < ls; ++i) {
            if (s[i] < s[i + 1]) {
                ++i;
                break;
            } else {
                s1.push_back(s[i]);
            }
        }
        while (s1.size() < ls - 1) {
            s1.push_back(s[i++]);
        }
        
        return s1;
    }
    
    bool comp(const string &s1, const string &s2, int i, int j) {
        int n1 = s1.size();
        int n2 = s2.size();
        while (i < n1 && j < n2) {
            if (s1[i] > s2[j]) {
                return true;
            }
            if (s1[i] < s2[j]) {
                return false;
            }
            ++i;
            ++j;
        }
        return j == n2;
    }
    
    string mergeTwo(const string &s1, const string &s2) {
        string s = "";
        int n1 = s1.size();
        int n2 = s2.size();
        int i, j;
        char ch;
        
        i = j = 0;
        while (i < n1 || j < n2) {
            if (i == n1) {
                ch = s2[j++];
            } else if (j == n2) {
                ch = s1[i++];
            } else if (comp(s1, s2, i, j)) {
                ch = s1[i++];
            } else {
                ch = s2[j++];
            }
            s.push_back(ch);
        }
        
        return s;
    }
};
