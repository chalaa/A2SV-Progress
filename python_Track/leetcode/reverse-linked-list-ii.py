# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        temp = dummy
        for i in range(left-1):
            temp = temp.next
        temp2 = temp.next
        temp.next = None
        new_head = None
        new_tail = None
        for i in range(right-left+1):
            node = temp2
            temp2 = temp2.next
            if not new_head:
                new_head = node
                new_tail = node
            else:
                node.next = new_head
                new_head = node
        temp.next = new_head
        new_tail.next = temp2
        head = dummy.next
        return head

        


        