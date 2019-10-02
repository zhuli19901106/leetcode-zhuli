class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.length(), m = str2.length();
        int dp[n+1][m+1];
        for (int i = 0; i <= n; ++i)
        {
            for (int j = 0; j <= m; ++j)
                dp[i][j] = 5000;
        }
        pair <int, int> parent[n+1][m+1];
        char character[n+1][m+1];
        dp[0][0] = 0;
        for (int i = 0; i <= n; ++i)
        {
            for (int j = 0; j <= m; ++j)
            {
                if (i == n and j == m) continue;
                if (i == n)
                {
                    if (dp[i][j+1] > dp[i][j] + 1)
                    {
                        dp[i][j+1] = dp[i][j] + 1;
                        parent[i][j+1] = {i,j};
                        character[i][j+1] = str2[j];
                    }
                    continue;
                }
                if (j == m)
                {
                    if (dp[i+1][j] > dp[i][j] + 1)
                    {
                        dp[i+1][j] = dp[i][j] + 1;
                        parent[i+1][j] = {i,j};
                        character[i+1][j] = str1[i];
                    }
                    continue;
                }
                char c1 = str1[i], c2 = str2[j];
                if (c1 == c2)
                {
                    if (dp[i+1][j+1] > dp[i][j] + 1)
                    {
                        dp[i+1][j+1] = dp[i][j] + 1;
                        parent[i+1][j+1] = {i,j};
                        character[i+1][j+1] = c1;
                    }
                }
                
                if (dp[i+1][j] > dp[i][j] + 1)
                {
                    dp[i+1][j] = dp[i][j] + 1;
                    parent[i+1][j] = {i,j};
                    character[i+1][j] = c1;
                }
                
                if (dp[i][j+1] > dp[i][j] + 1)
                {
                    dp[i][j+1] = dp[i][j] + 1;
                    parent[i][j+1] = {i,j};
                    character[i][j+1] = c2;
                }
            }
        }
        int i = n, j = m;
        string ans = "";
        while (i > 0 or j > 0)
        {
            ans += character[i][j];
            int x,y;
            x = parent[i][j].first;
            y = parent[i][j].second;
            i = x; j = y;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
