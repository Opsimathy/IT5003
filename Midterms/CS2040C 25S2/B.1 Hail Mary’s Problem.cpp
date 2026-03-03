#include <iostream>
using namespace std;

class Solution {
public:
    bool is_sorted_minimal_fix(vector<string>& words, string order) {
        vector<string> sorted_words = words;
        sort(sorted_words.begin(), sorted_words.end(), [&order](string a, string b) {
            int i = 0, n = (int)a.size(), j = 0, m = (int)b.size();
            while (i < n and j < m) {
                int o1 = order.find(a[i++]), o2 = order.find(b[j++]);
                if (o1 < o2)
                    return true;
                else if (o1 > o2)
                    return false;
            }
            return n <= m;
        });
        return sorted_words == words;
    }

    bool is_sorted_optimal(vector<string>& words, string order) {
        int r[26];
        for (int i = 0; i < 26; i++)
            r[order[i] - 'a'] = i;
        auto leq = [&](const string& a, const string& b) {
            int i = 0, n = (int)a.size(), m = (int)b.size();
            while (i < n && i < m) {
                int ra = r[a[i] - 'a'], rb = r[b[i] - 'a'];
                if (ra < rb)
                    return true;
                else if (ra > rb)
                    return false;
                i++;
            }
            return n <= m;
        };
        for (int i = 0; i + 1 < (int)words.size(); ++i)
            if (!leq(words[i], words[i + 1]))
                return false;
        return true;
    }
};

int main() {
    Solution sol;
    vector<string> v1 = {"you", "where", "question"};
    vector<string> v2 = {"i", "dont", "understand"};
    vector<string> v3 = {"you", "come", "from", "where", "question"};
    vector<string> v4 = {"oh", "sol", "star"};
    vector<string> v5 = {"solaris", "sol"};
    vector<string> v6 = {"s", "s"};
    string s1 = "ybcfwdqazxletrpkmnhgijousv", s2 = "abcdefghijklmnopqrstuvwxyz";
    cout << sol.is_sorted_minimal_fix(v1, s1) << endl;
    cout << sol.is_sorted_minimal_fix(v2, s2) << endl;
    cout << sol.is_sorted_minimal_fix(v3, s1) << endl;
    cout << sol.is_sorted_minimal_fix(v4, s2) << endl;
    cout << sol.is_sorted_minimal_fix(v5, s2) << endl;
    cout << sol.is_sorted_minimal_fix(v6, s1) << endl;
    cout << endl;
    cout << sol.is_sorted_optimal(v1, s1) << endl;
    cout << sol.is_sorted_optimal(v2, s2) << endl;
    cout << sol.is_sorted_optimal(v3, s1) << endl;
    cout << sol.is_sorted_optimal(v4, s2) << endl;
    cout << sol.is_sorted_optimal(v5, s2) << endl;
    cout << sol.is_sorted_optimal(v6, s1) << endl;
    return 0;
}
/*1 0 1 1 0 1*/
