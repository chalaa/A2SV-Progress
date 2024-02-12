# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        _set = set()
        
        while headA.next or headB.next:
            if headA and headA in _set:
                return headA
            if headA.next:
                _set.add(headA)
                headA = headA.next
            if headB and headB in _set:
                return headB
            if headB.next:
              _set.add(headB)
              headB = headB.next
        if headA == headB:
            return headA
