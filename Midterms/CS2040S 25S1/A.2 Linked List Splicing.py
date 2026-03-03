# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splice(self, head1: Optional[ListNode],
               tail1: Optional[ListNode],
               head2: Optional[ListNode],
               tail2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0, head1)
        pre = dum
        cur = head1
        while cur:
            if (cur.val == 2 and cur.next.val == 0 and cur.next.next.val == 4
                and cur.next.next.next.val == 0):
                pre.next = head2
                tail2.next = cur.next.next.next.next
                break
            pre = cur
            cur = cur.next
        return dum.next


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_tail(head):
    if not head:
        return None
    while head.next:
        head = head.next
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


tests = [[[1, 1, 0, 1, 7, 2, 0, 4, 0, 7, 3, 2, 3, 0], [71, 72, 73, 74, 75]],
         [[2, 0, 4, 0, 9, 9], [8, 8, 8, 8]],
         [[5, 6, 2, 0, 4, 0], [1, 2, 3, 4]],
         [[9, 1, 2, 0, 4, 0, 3, 3, 3], [10, 20, 30, 40]]]

for SLL1, SLL2 in tests:
    head1 = build(SLL1)
    tail1 = to_tail(head1)
    head2 = build(SLL2)
    tail2 = to_tail(head2)
    _ = to_list(Solution().splice(head1, tail1, head2, tail2))
    print(f"{SLL1}, {SLL2} -> {_}")
'''
[1, 1, 0, 1, 7, 2, 0, 4, 0, 7, 3, 2, 3, 0], [71, 72, 73, 74, 75] ->
[1, 1, 0, 1, 7, 71, 72, 73, 74, 75, 7, 3, 2, 3, 0]
[2, 0, 4, 0, 9, 9], [8, 8, 8, 8] -> [8, 8, 8, 8, 9, 9]
[5, 6, 2, 0, 4, 0], [1, 2, 3, 4] -> [5, 6, 1, 2, 3, 4]
[9, 1, 2, 0, 4, 0, 3, 3, 3], [10, 20, 30, 40] -> [9, 1, 10, 20, 30, 40, 3, 3, 3]
'''
