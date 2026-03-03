# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import Optional

    @staticmethod
    def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = node
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head = Solution.reverse(head)
        dum = ListNode(0, head)
        pre = dum
        cur = head
        msf = float('inf')
        while cur:
            if cur.val > msf:
                pre.next = cur.next
            else:
                msf = cur.val
                pre = cur
            cur = cur.next
        return Solution.reverse(dum.next)


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


tests = [[], [7], [1, 2, 3, 4], [4, 3, 2, 1], [5, 2, 13, 3, 8],
         [2, 2, 2], [10, 5, 10], [1, 1, 1, 2], [9, 1, 2, 3, 0],
         [1, 90, 19, 1, 73, 15, 70]]
for t in tests:
    print(f"{t} -> {to_list(Solution().removeNodes(build(t)))}")
