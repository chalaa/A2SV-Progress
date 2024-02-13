# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            new_node = ListNode(head.val)
            head = head.next

            if not new_head:
                new_head = new_node
            else:
                dummy = ListNode(100000,new_head)
                temp = dummy
                while temp.next and temp.next.val < new_node.val:
                    temp = temp.next
                if temp.next:
                    new_node.next = temp.next
                    temp.next = new_node
                else:
                    temp.next = new_node
                new_head = dummy.next
        return new_head
            
        
        