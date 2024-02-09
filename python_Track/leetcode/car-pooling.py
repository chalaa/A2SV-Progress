class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix_sum = [0] * 1002

        for trip in trips:
            passengers, start, end = trip
            prefix_sum [start] += passengers
            prefix_sum [end] -= passengers
        
        for i in range(1,1002):
            prefix_sum[i] += prefix_sum[i-1]
        
        if max(prefix_sum) > capacity:
            return False
        return True