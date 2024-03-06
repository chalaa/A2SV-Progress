class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowerBound = max(weights)
        upperBound = sum(weights)
        best = -1
        while lowerBound <= upperBound:
            mid = lowerBound + (upperBound-lowerBound)//2
            calculated_day = 0
            capacity = 0
            for i in weights:
                if capacity + i > mid:
                    calculated_day += 1
                    capacity = i
                    continue
                capacity += i
            if capacity:
                calculated_day += 1


            if calculated_day > days:
                lowerBound = mid+1
            else:
                upperBound = mid-1
                best= mid
        return best
            