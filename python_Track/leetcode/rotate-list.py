# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1 
        k %= length
        temp2 = head
        for i in range(length-k-1):
            temp2 = temp2.next
        temp.next = head
        head = temp2.next
        temp2.next = None
        return head    
        