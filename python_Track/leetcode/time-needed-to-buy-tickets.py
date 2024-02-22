class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            if i < k:
                if tickets[i] >= tickets[k]:
                    ans += tickets[k]
                else:
                    ans += tickets[i]
            elif i > k:
                if tickets[i] >= tickets[k]:
                    ans += tickets[k] -1
                else:
                    ans += tickets[i]
            else:
                ans += tickets[k]
        return ans
        