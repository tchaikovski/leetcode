# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> \
    Optional[ListNode]:

        dummy = ListNode('i')
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


xx = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 4, 5, 6, 7]

# list1 = []
# list2 = [0]
print(xx.mergeTwoLists(list1, list2))
