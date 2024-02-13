# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n<0 or not head:
            return head
        if not head.next:
            return None
        temp = head
        count = head
        ct=0
        while (count):
            ct+=1
            count=count.next
        print(ct)
        if ct-n ==0 :
            return head.next
        else:
            for i in range(1,ct-n):
                temp=temp.next
        temp.next=temp.next.next
        return head
       