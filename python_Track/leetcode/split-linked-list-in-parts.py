# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        while temp:
            length +=1
            temp = temp.next
        ans = []
        if length <= k:
            for i in range(length):
                temp = head
                head = head.next
                temp.next = None
                ans.append(temp)
            for i in range(k - length):
                ans.append(None)
        else:
            n = length // k
            mod = length % k
            while length:
                m = n
                if mod:
                    m += 1
                    mod -= 1
                temp = head
                for i in range(m-1):
                    temp = temp.next
                temp2 = head
                head = temp.next
                temp.next = None
                ans.append(temp2)
                length -= m
        return ans
