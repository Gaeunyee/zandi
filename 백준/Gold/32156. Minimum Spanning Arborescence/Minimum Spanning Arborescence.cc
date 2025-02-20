#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int N, M, r;
    cin >> N >> M >> r;
    
    vector<vector<pii>> graph(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        graph[u].emplace_back(c, v);
    }
    
    queue<int> qu;
    vector<bool> visited(N + 1, false);
    qu.push(r);
    visited[r] = true;
    int able = 1;
    vector<pii> edge;
    
    while (!qu.empty()) {
        int t = qu.front();
        qu.pop();
        for (auto &[cost, v] : graph[t]) {
            edge.emplace_back(cost, v);
            if (!visited[v]) {
                visited[v] = true;
                qu.push(v);
                able++;
            }
        }
    }
    
    if (able < N) {
        cout << -1 << "\n";
        return 0;
    }
    
    fill(visited.begin(), visited.end(), false);
    visited[r] = true;
    
    sort(edge.begin(), edge.end());
    long long res = 0;
    
    for (auto &[c, v] : edge) {
        if (!visited[v]) {
            res += c;
            visited[v] = true;
        }
    }
    
    cout << res << "\n";
    return 0;
}
