#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 100000 * 2;

int N;
vector<int> db;
vector<vector<int>> graph;
vector<vector<int>> dp;
vector<bool> inv;

void dfs(int t) {
    dp[t][0] = 0;
    dp[t][1] = db[t];

    for (int nxt : graph[t]) {
        dfs(nxt);
        dp[t][0] += max(dp[nxt][0], dp[nxt][1]);
        dp[t][1] += dp[nxt][0];
    }
}

void backTrack(int t) {
    for (int nxt : graph[t]) {
        if (inv[t]) {
            backTrack(nxt);
        } else {
            if (dp[nxt][0] < dp[nxt][1]) {
                inv[nxt] = true;
            }
            backTrack(nxt);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    db.resize(N + 1);
    graph.resize(N + 1);
    dp.assign(N + 1, vector<int>(2, 0));
    inv.assign(N + 1, false);

    for (int i = 1; i <= N; ++i) {
        cin >> db[i];
    }

    for (int i = 2; i <= N; ++i) {
        int parent;
        cin >> parent;
        graph[parent].push_back(i);
    }

    dfs(1);
    cout << dp[1][1] << " " << dp[1][0] << "\n";

    inv[1] = true;
    backTrack(1);
    for (int i = 1; i <= N; ++i) {
        if (inv[i]) {
            cout << i << " ";
        }
    }
    cout << -1 << "\n";

    inv.assign(N + 1, false);
    backTrack(1);
    for (int i = 1; i <= N; ++i) {
        if (inv[i]) {
            cout << i << " ";
        }
    }
    cout << -1 << "\n";

    return 0;
}
