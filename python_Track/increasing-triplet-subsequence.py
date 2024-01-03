class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mins = []
        maxs = []
        for i in range(1,len(nums)-1):
            if len(mins) == 0:
                mins.append(nums[i-1])
            else:
                mins.append(min(nums[i-1],mins[-1]))
        for i in range(len(nums)-2,0,-1):
            if len(maxs) == 0:
                maxs.append(nums[i+1])
            else:
                maxs.append(max(nums[i+1],maxs[-1]))
        maxs.reverse()
        for i in range(1,len(nums)-1):
            if mins[i-1] < nums[i] < maxs[i-1]:
                return True
        return False