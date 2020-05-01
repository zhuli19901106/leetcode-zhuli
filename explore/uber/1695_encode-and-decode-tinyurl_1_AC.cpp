// You see, it's stateless, isn't it?
// One liner joke :)
// With the given charset, I think the feasibility of using a string lossless 
// compression algorithm to shorten the url is really questionable.
// Otherwise, how is it gonna be stateless anyway?
class Solution {
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        return longUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return shortUrl;
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
