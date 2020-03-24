// You don't need to deal with the "and".
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    Solution() {
        um[0] = "Zero";
        um[1] = "One";
        um[2] = "Two";
        um[3] = "Three";
        um[4] = "Four";
        um[5] = "Five";
        um[6] = "Six";
        um[7] = "Seven";
        um[8] = "Eight";
        um[9] = "Nine";
        um[10] = "Ten";
        um[11] = "Eleven";
        um[12] = "Twelve";
        um[13] = "Thirteen";
        um[14] = "Fourteen";
        um[15] = "Fifteen";
        um[16] = "Sixteen";
        um[17] = "Seventeen";
        um[18] = "Eighteen";
        um[19] = "Nineteen";
        um[20] = "Twenty";
        um[30] = "Thirty";
        um[40] = "Forty";
        um[50] = "Fifty";
        um[60] = "Sixty";
        um[70] = "Seventy";
        um[80] = "Eighty";
        um[90] = "Ninety";
        um[100] = "Hundred";
    }
    
    string numberToWords(int num) {
        vector<string> v;
        say(num, v);
        string res = "";
        for (string &s: v) {
            res += s;
            res.push_back(' ');
        }
        res.pop_back();
        v.clear();
        
        return res;
    }
    
    ~Solution() {
        um.clear();
    }
private:
    unordered_map<int, string> um;
    
    void say(int num, vector<string> &v) {
        static const string scale[3] = {"Billion", "Million", "Thousand"};
        int i = 0;
        int b10 = 1000000000;
        while (b10 > 1) {
            if (num >= b10) {
                say(num / b10, v);
                v.push_back(scale[i]);
                num %= b10;
            }
            ++i;
            b10 /= 1000;
        }
        
        if (num == 0 && v.size() == 0) {
            v.push_back(um[num]);
            return;
        }
        
        b10 = 100;
        if (num >= b10) {
            v.push_back(um[num / b10]);
            v.push_back(um[b10]);
            num %= b10;
        }
        if (num == 0) {
            return;
        }
        if (um.find(num) != um.end()) {
            v.push_back(um[num]);
        } else {
            v.push_back(um[num / 10 * 10]);
            v.push_back(um[num % 10]);
        }
    }
};
