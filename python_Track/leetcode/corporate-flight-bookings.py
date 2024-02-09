class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefix_sum = [0]*(n+1)

        for booking in bookings:
            first,last,seat = booking
            prefix_sum[first-1] += seat
            prefix_sum[last] -= seat

        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
            
        return prefix_sum[:-1]