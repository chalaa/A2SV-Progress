# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        tail = None
        while list1 and list2:
            if list1.val < list2.val:
                if not head:
                    head = list1
                    tail = head
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    tail = head
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next
        while list1:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        while list2:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        
        return head
