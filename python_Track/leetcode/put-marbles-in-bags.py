class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ## collect the posible adjecent elements sum
        n = len(weights)
        pair_weight = []
        for i in range(n-1):
            pair_weight.append(weights[i]+weights[i+1])
        pair_weight.sort()
        ans = 0
        for i in range(k-1):
            ans += pair_weight[n-2-i] - pair_weight[i]
        return ans