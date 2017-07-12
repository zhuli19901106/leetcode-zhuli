/*
// Calculate palindrome product for 2 n-digit numbers.
#include <cmath>
#include <cstdint>
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
using std::pow;

int64_t getPal(int64_t n)
{
	const int R = 10;
	
	if (n <= 0) {
		return 0;
	}
	int64_t n0 = n;
	int64_t n1 = 0;
	while (n > 0) {
		n1 = n1 * R + (n % R);
		n0 *= R;
		n /= R;
	}
	return n0 + n1;
}

int64_t solve(int n)
{
	if (n == 1) {
		return 9;
	}
	int64_t low, high;
	int64_t num;
	int64_t pal;
	int64_t i;

	low = (int64_t)pow(10, n - 1);
	high = (int64_t)pow(10, n) - 1;
	for (num = high; num >= low; --num) {
		pal = getPal(num);
		for (i = high; pal / i <= high && i >= low; --i) {
			if (pal % i == 0) {
				// cout << "(" << i << ", " << pal / i << ")";
				return pal;
			}
		}
	}
	return 0;
}

int main()
{
	int n;
	int64_t pal;
	
	for (n = 1; n <= 8; ++n) {
		pal = solve(n);
		cout << pal << ", ";
	}
	cout << endl;

	return 0;
}
*/
#include <cstdint>

int64_t a[] = {9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999};

class Solution {
public:
    int largestPalindrome(int n) {
        return a[n - 1] % 1337;
    }
};
