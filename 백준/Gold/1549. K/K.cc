#include <iostream>
#include <vector>
#include <cmath>
#include <climits>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> lst(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        long long num;
        cin >> num;
        lst[i] = lst[i - 1] + num;
    }

    long long m = LLONG_MAX;
    int K = -1;

    for (int k = N / 2; k > 0; --k) {
        for (int i = 1; i <= N - 2 * k+1; ++i) {
            for (int j = i + k; j <= N - k + 1; ++j) {
                long long t = abs((lst[j + k - 1] - lst[j - 1]) - (lst[i + k - 1] - lst[i - 1]));
                if (m > t) {
                    m = t;
                    K = k;
                }
            }
        }
    }

    cout << K << "\n";
    cout << m << "\n";

    return 0;
}