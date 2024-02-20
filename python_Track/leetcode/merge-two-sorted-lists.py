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
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next =self.mergeTwoLists(list1,list2.next)
            return list2
        # head = None
        # tail = None
        # def merge(list1,list2):
        #     nonlocal head
        #     nonlocal tail
        #     if list1.val < list2.val:
        #         if not head:
        #             head = list1
        #             tail = head
        #         else:
        #             tail.next = list1
        #             tail = tail.next
        #     else:
        #         if not head:
        #             head = list2
        #             tail = head
        #         else:
        #             tail.next = list2
        #             tail = tail.next
        # while list1 and list2:
        #     merge(list1,list2)
        #     if list1.val < list2.val:
        #         list1=list1.next
        #     else:
        #         list2=list2.next
        # if list1:
        #     tail.next = list1
        # if list2:
        #     tail.next = list2

        # return head
