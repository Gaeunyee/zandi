#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

void FailureFunction(const string& pattern, vector<int>& F) {
    int N = pattern.size();
    int j = 0;
    for (int i = 1; i < N; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = F[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            F[i] = j + 1;
            j++;
        }
        else {
            F[i] = 0;
        }
    }
}

bool KMP(deque<char>& qu, const string& pattern, vector<int>& F, vector<pair<int, char>>& st, int j, vector<pair<int, char>>& nst) {
    while (!qu.empty()) {
        if (qu.front() == pattern[j]) {
            j++;
            st.emplace_back(j, qu.front());
            qu.pop_front();
            if (j == pattern.size()) {
                return true;
            }
        }
        else if (j > 0) {
            j = F[j - 1];
        }
        else {
            st.emplace_back(j, qu.front());
            qu.pop_front();
            j = 0;
        }
    }

    while (nst.size() > 1) {
        if (nst.back().second == pattern[j]) {
            j++;
            st.emplace_back(j, nst.back().second);
            nst.pop_back();
            if (j == pattern.size()) {
                return true;
            }
        }
        else if (j > 0) {
            j = F[j - 1];
        }
        else {
            j = 0;
            st.emplace_back(j, nst.back().second);
            nst.pop_back();
        }
    }
    return false;
}

bool reversed_KMP(deque<char>& qu, const string& pattern, vector<int>& F, vector<pair<int, char>>& st, int j, vector<pair<int, char>>& nst) {
    while (!qu.empty()) {
        if (qu.back() == pattern[j]) {
            j++;
            st.emplace_back(j, qu.back());
            qu.pop_back();
            if (j == pattern.size()) {
                return true;
            }
        }
        else if (j > 0) {
            j = F[j - 1];
        }
        else {
            st.emplace_back(j, qu.back());
            qu.pop_back();
            j = 0;
        }
    }

    while (nst.size() > 1) {
        if (nst.back().second == pattern[j]) {
            j++;
            st.emplace_back(j, nst.back().second);
            nst.pop_back();
            if (j == pattern.size()) {
                return true;
            }
        }
        else if (j > 0) {
            j = F[j - 1];
        }
        else {
            st.emplace_back(j, nst.back().second);
            nst.pop_back();
            j = 0;
        }
    }
    return false;
}

int main() {
    string A;
    cin >> A;
    int N = A.size();
    vector<int> F1(N, 0), F2(N, 0);

    string rA = A;
    reverse(rA.begin(), rA.end());

    FailureFunction(A, F1);
    FailureFunction(rA, F2);

    string line;
    cin >> line;
    deque<char> qu(line.begin(), line.end());
    vector<pair<int, char>> l_st = { {0, '\0'} }, r_st = { {0, '\0'} };

    int flag = 1;
    while (true) {
        if (flag == 1) {
            if (KMP(qu, A, F1, l_st, l_st.back().first, r_st)) {
                for (int i = 0; i < N; i++) l_st.pop_back();
            }
            else {
                break;
            }
        }
        else {
            if (reversed_KMP(qu, rA, F2, r_st, r_st.back().first, l_st)) {
                for (int i = 0; i < N; i++) r_st.pop_back();
            }
            else {
                break;
            }
        }
        flag *= -1;
    }

    for (size_t i = 1; i < l_st.size(); i++) {
        cout << l_st[i].second;
    }
    for (int i = r_st.size() - 1; i > 0; i--) {
        cout << r_st[i].second;
    }
    cout << endl;
    return 0;
}
