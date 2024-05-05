#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        if (is_sorted(a.begin(), a.end())) {
            vector<int> ans(1, 1);
            vector<long long> pref(1, a[0]);
            for (int i = 1; i < n; ++i) {
                int ans1 = 1;
                if (a[i] <= pref.back() << 1) {
                    ans1 += ans.back();
                }
                pref.back() += a[i];
                ans.push_back(ans1);
            }
            for (int x : ans) {
                cout << x << " ";
            }
            cout << '\n';
        } else {
            vector<int> v;
            vector<int> ans;
            for (int i = 0; i < n; ++i) {
                v.push_back(a[i]);
                sort(v.begin(), v.end());
                int ans2 = 1;
                vector<long long> pref(1, v[0]);
                for (int j = 1; j <= i; ++j) {
                    int ans1 = 1;
                    if (v[j] <= pref.back() << 1) {
                        ans1 += ans2;
                    }
                    pref.back() += v[j];
                    ans2 = ans1;
                }
                ans.push_back(ans2);
            }
            for (int x : ans) {
                cout << x << " ";
            }
            cout << '\n';
        }
    }
    return 0;
}
