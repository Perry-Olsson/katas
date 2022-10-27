from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def from_list(list: List[int]) -> ListNode:
    if len(list) <= 0:
        return ListNode()

    head = ListNode(list[0])
    prev = head
    for i in range(1, len(list)):
        cur = ListNode(list[i])
        prev.next = cur 
        prev = cur
    return head

def to_list(ll: Optional[ListNode]) -> List[int]:
    ret_list = []
    cur = ll
    while cur is not None:
        ret_list.append(cur.val)
        cur = cur.next

    return ret_list





class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self._improved(list1, list2)

    def _improved(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        dummy_head = ListNode(0)
        cur = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2
        return dummy_head.next

    def working_impl(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list2

        cur1 = list1
        cur2 = list2
        new_head = None
        if cur1.val < cur2.val:
            new_head = cur1
            cur1 = cur1.next
        else:
            new_head = cur2
            cur2 = cur2.next

        new_head.next = None
        new_cur = new_head
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                new_cur.next = cur1
                cur1 = cur1.next
            else:
                new_cur.next = cur2
                cur2 = cur2.next

            new_cur = new_cur.next
            new_cur.next = None

        if cur1 is not None:
            new_cur.next = cur1
        else:
            new_cur.next = cur2


        return new_head



