class Solution {
public:
    string intToRoman(int num) {
        static const string letters = "IVXLCDM";
        static const int n = letters.size();
        static const string comb[] = {
            "",
            "0",
            "00",
            "000",
            "01",
            "1",
            "10",
            "100",
            "1000",
            "02"
        };
        
        int d;
        int i, j;
        int len;
        int base = 1000;
        string res = "";
        
        j = n - 1;
        while (base > 0) {
            d = num / base;
            num %= base;
            base /= 10;
            
            len = comb[d].size();
            for (i = 0; i < len; ++i) {
                res.push_back(letters[j + comb[d][i] - '0']);
            }
            j -= 2;
        }
        return res;
    }
};
