class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # ans = 0
        # for i in range(len(tickets)):
        #     if i < k:
        #         if tickets[i] >= tickets[k]:
        #             ans += tickets[k]
        #         else:
        #             ans += tickets[i]
        #     elif i > k:
        #         if tickets[i] >= tickets[k]:
        #             ans += tickets[k] -1
        #         else:
        #             ans += tickets[i]
        #     else:
        #         ans += tickets[k]
        # return ans

        ## queue approach

        queue = deque()
        ans = 0
        for i in range(len(tickets)):
            x = tickets[i] - 1
            ans += 1
            if x == 0 and i == k:
                return ans
            if x > 0:
                queue.append([x,i])
        while queue:
            x = queue.popleft()
            x[0] -= 1
            ans += 1
            if x[0] == 0 and x[1] == k:
                return ans
            if x[0] > 0:
                queue.append(x)

        