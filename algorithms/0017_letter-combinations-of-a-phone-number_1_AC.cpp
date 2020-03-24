class Solution {
public:
    Solution() {
        letters.push_back("");
        letters.push_back("");
        letters.push_back("abc");
        letters.push_back("def");
        letters.push_back("ghi");
        letters.push_back("jkl");
        letters.push_back("mno");
        letters.push_back("pqrs");
        letters.push_back("tuv");
        letters.push_back("wxyz");
    }
    
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.size() == 0) {
            return res;
        }
        string s = "";
        dfs(s, digits, res);
        return res;
    }
private:
    vector<string> letters;
    
    void dfs(string &s, string &digits, vector<string> &res) {
        int idx = s.size();
        if (idx == digits.size()) {
            res.push_back(s);
            return;
        }
        
        int i;
        int d = digits[idx] - '0';
        for (i = 0; i < letters[d].size(); ++i) {
            s.push_back(letters[d][i]);
            dfs(s, digits, res);
            s.pop_back();
        }
    }
};
