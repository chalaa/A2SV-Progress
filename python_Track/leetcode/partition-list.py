# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = None
        left_tail = None
        right = None
        right_tail = None
        while head:
            temp = head
            head = head.next
            temp.next = None
            if temp.val < x:
                if not left:
                    left = temp
                    left_tail = left
                else:
                    left_tail.next = temp
                    left_tail = left_tail.next
            else:
                if not right:
                    right = temp
                    right_tail = right
                else:
                    right_tail.next = temp
                    right_tail = right_tail.next
        if left:
            left_tail.next = right
            return left
        return right

        