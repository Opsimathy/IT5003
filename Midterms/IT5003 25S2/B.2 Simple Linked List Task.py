# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = [0] * 100
        cur = head
        while cur:
            count[cur.val] += 1
            cur = cur.next
        dum = ListNode(0)
        dum.next = head
        pre = dum
        cur = head
        while cur:
            if count[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dum.next


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


tests = [[2, 3, 6, 7, 2, 3, 4, 1, 10, 2, 9, 6]]
for t in tests:
    print(f"{t} -> {to_list(Solution().removeNodes(build(t)))}")
"""[2, 3, 6, 7, 2, 3, 4, 1, 10, 2, 9, 6] -> [7, 4, 1, 10, 9]"""
