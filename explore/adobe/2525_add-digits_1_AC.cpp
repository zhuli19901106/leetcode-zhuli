// Digital root.
class Solution {
public:
    int addDigits(int num) {
        return num > 0 ? (num + 8) % 9 + 1 : 0;
    }
};
