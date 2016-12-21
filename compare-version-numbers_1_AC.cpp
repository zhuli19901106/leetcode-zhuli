class Solution {
public:
    int compareVersion(string version1, string version2) {
        int n1 = version1.size();
        int n2 = version2.size();
        string tk1, tk2;
        int i1, i2;
        int res;
        
        i1 = 0;
        i2 = 0;
        while (i1 < n1 && i2 < n2) {
            tk1 = nextToken(version1, i1);
            tk2 = nextToken(version2, i2);
            res = compare(tk1, tk2);
            if (res != 0) {
                return res;
            }
        }
        while (i1 < n1) {
            tk1 = nextToken(version1, i1);
            if (compare(tk1, "0") > 0) {
                return +1;
            }
        }
        while (i2 < n2) {
            tk2 = nextToken(version2, i2);
            if (compare(tk2, "0") > 0) {
                return -1;
            }
        }
        
        if (i1 < n1) {
            return +1;
        }
        if (i2 < n2) {
            return -1;
        }
        return 0;
    }
private:
    string nextToken(const string &s, int &i) {
        int n = s.size();
        string tk = "";
        while (i < n && s[i] == '0') {
            ++i;
        }
        if (i >= n || s[i] == '.') {
            --i;
        }
        
        while (i < n && s[i] != '.') {
            tk.push_back(s[i++]);
        }
        ++i;
        return tk;
    }
    
    int compare(const string &s1, const string &s2) {
        int l1 = s1.size();
        int l2 = s2.size();
        if (l1 < l2) {
            return -1;
        }
        if (l1 > l2) {
            return +1;
        }
        return s1 < s2 ? -1 : (s1 > s2 ? +1 : 0);
    }
};
