#include <iostream>
using namespace std;

class Solution {
public:
    pair<int, int> earliestMeeting_minimal_fix(vector<pair<int, int>>& free1,
                                               vector<pair<int, int>>& free2,
                                               int duration) {
        int bestStart = INT_MAX;
        for (int i = 0; i < (int)free1.size(); i++)
            for (int j = 0; j < (int)free2.size(); j++) {
                int start = max(free1[i].first, free2[j].first);
                int end = min(free1[i].second, free2[j].second);
                if (end - start >= duration)
                    bestStart = min(bestStart, start);
            }
        if (bestStart == INT_MAX)
            return {-1, -1};
        return {bestStart, bestStart + duration};
    }

    pair<int, int> earliestMeeting_optimal(vector<pair<int, int>>& free1,
                                           vector<pair<int, int>>& free2,
                                           int duration) {
        std::vector<int> a(1440, 0);
        for (auto [s,e] : free1)
            for (int t = s; t < e; t++)
                a[t]++;
        for (auto [s,e] : free2)
            for (int t = s; t < e; t++)
                a[t]++;
        for (int t = 0, r = 0; t < 1440; t++) {
            r = a[t] == 2 ? r + 1 : 0;
            if (r == duration)
                return {t - duration + 1, t + 1};
        }
        return {-1, -1};
    }
};

int main() {
    Solution sol;
    vector<pair<int, int>> f1 = {{610, 650}, {740, 810}, {660, 720}},
                           f2 = {{660, 670}, {600, 615}};
    int d1 = 8, d2 = 11;
    auto s1 = sol.earliestMeeting_minimal_fix(f1, f2, d1);
    auto s2 = sol.earliestMeeting_minimal_fix(f1, f2, d2);
    auto s3 = sol.earliestMeeting_optimal(f1, f2, d1);
    auto s4 = sol.earliestMeeting_optimal(f1, f2, d2);
    cout << s1.first << ' ' << s1.second << endl;
    cout << s2.first << ' ' << s2.second << endl;
    cout << s3.first << ' ' << s3.second << endl;
    cout << s4.first << ' ' << s4.second << endl;
    return 0;
}
/*660 668
-1 -1*/
