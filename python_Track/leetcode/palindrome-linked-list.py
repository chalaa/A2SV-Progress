# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp
        if fast:
            slow = slow.next
        while rev and slow:
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
