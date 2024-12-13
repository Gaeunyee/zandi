#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;


int isTriangle(long double a, long double b, long double c) {
    vector<long double> l = {a, b, c};
    sort(l.begin(), l.end());
    if (l[2] < l[0] + l[1]) {
        return 1; 
    } else if (l[2] == l[0] + l[1]) {
        return 0; 
    }
    return -1; 
}


bool solve(const vector<vector<long double>>& matrix) {
    long double i, j, k;
    long double a, b, c;
    long double x1, y1, x2, y2;

    
    i = 0; j = 1; k = 2;
    a = matrix[i][j]; b = matrix[k][i]; c = matrix[j][k];
    int t = isTriangle(a, b, c);
    if (t == -1) return false;
    x1 = (a * a + b * b - c * c) / (2 * a);
    y1 = sqrt(b * b - x1 * x1);
    

    
    i = 0; j = 1; k = 3;
    a = matrix[i][j]; b = matrix[k][i]; c = matrix[j][k];
    t = isTriangle(a, b, c);
    if (t == -1) return false;
    x2 = (a * a + b * b - c * c) / (2 * a);
    y2 = sqrt(b * b - x2 * x2);
    

    
    long double dist1 = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    long double dist2 = sqrt((x2 - x1) * (x2 - x1) + (y2 + y1) * (y2 + y1));
    return dist1 <= matrix[2][3] && matrix[2][3] <= dist2;
}

int main() {
    
    vector<vector<long double>> matrix(4, vector<long double>(4));
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> matrix[i][j];
        }
    }

  
    if (solve(matrix)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
