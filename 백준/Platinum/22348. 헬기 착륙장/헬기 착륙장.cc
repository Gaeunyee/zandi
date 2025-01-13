#include <iostream>
#include <vector>
using namespace std;

const int SIZE = 500;
const int LENGTH = 50000;
const int MOD = 1e9 + 7;

int dp[SIZE][LENGTH + 1];
int matrix[SIZE][LENGTH + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    // Initialize dp and matrix arrays
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j <= LENGTH; ++j) {
            dp[i][j] = 0;
            matrix[i][j] = 0;
        }
    }

    dp[0][0] = 1;
    int s_ab = 0;

    for (int i = 1; i < SIZE; ++i) {
        s_ab += i;
        for (int j = 0; j <= LENGTH; ++j) {
            if (s_ab - j <= LENGTH) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD;
            }
            if (j - i >= 0) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - i]) % MOD;
            }
        }
    }

    for (int i = 1; i < SIZE; ++i) {
        long long s = 0;
        for (int j = 0; j <= LENGTH; ++j) {
            s = (s + dp[i][j]) % MOD;
            matrix[i][j] = s;
        }
    }

    while (T--) {
        int a, b;
        cin >> a >> b;

        s_ab = 1;
        long long res = 0;
        int i = 1;

        while (s_ab <= a + b && i < SIZE) {
            if (s_ab > b) {
                if (s_ab - b > a) break;
                long long upper = matrix[i][a];
                long long lower = matrix[i][s_ab - b - 1];
                res = (res + upper - lower + MOD) % MOD;
            } else {
                res = (res + matrix[i][a]) % MOD;
            }
            ++i;
            s_ab += i;
        }

        cout << res << "\n";
    }

    return 0;
}