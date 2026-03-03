#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    vector<ListNode*> split_SLL(ListNode* head, int k) {
        int n = 0;
        ListNode* cur = head;
        while (cur != NULL) {
            ++n;
            cur = cur->next;
        }
        int size_per_part = n / k;
        vector<ListNode*> ans(k, NULL);
        cur = head;
        for (int i = 0; i < k; ++i) {
            ans[i] = cur;
            int cur_part_sz = size_per_part + (i < n % k);
            while (cur_part_sz-- > 1 && cur != NULL)
                cur = cur->next;
            if (cur != NULL) {
                ListNode* temp = cur->next;
                cur->next = NULL;
                cur = temp;
            }
        }
        return ans;
    }
};

ListNode* build(const vector<int>& a) {
    ListNode dum(0);
    ListNode* cur = &dum;
    for (int x : a) {
        cur->next = new ListNode(x);
        cur = cur->next;
    }
    return dum.next;
}

void printParts(const vector<ListNode*>& parts) {
    for (auto head : parts) {
        cout << "[";
        while (head) {
            cout << head->val;
            head = head->next;
            if (head) cout << ",";
        }
        cout << "] ";
    }
    cout << "\n";
}

int main() {
    Solution sol;
    printParts(sol.split_SLL(
        build({-61,45,-89,16,12,-69,-61,23,-83,-34,-50,91}), 3));
    printParts(sol.split_SLL(
        build({-61,45,-89,16,12,-69,-61,23,-83,-34,-50,91}), 4));
    printParts(sol.split_SLL(
        build({-61,45,-89,16,12,-69,-61,23,-83,-34,-50,91}), 5));
    printParts(sol.split_SLL(
        build({1,2,3,4,5,6,7}), 3));
    printParts(sol.split_SLL(
        build({9,8,7,6}), 4));
    printParts(sol.split_SLL(
        build({-5}), 1));
    printParts(sol.split_SLL(
        build({}), 1));
    return 0;
}
/*
[-61,45,-89,16] [12,-69,-61,23] [-83,-34,-50,91] 
[-61,45,-89] [16,12,-69] [-61,23,-83] [-34,-50,91] 
[-61,45,-89] [16,12,-69] [-61,23] [-83,-34] [-50,91] 
[1,2,3] [4,5] [6,7] 
[9] [8] [7] [6] 
[-5] 
[]
*/
