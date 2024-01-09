class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ct=0
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]+nums[j] == k):
                ct = ct+1
                i+=1
                j-=1
            elif(nums[i]+nums[j] > k):
                j=j-1
            else:
                i=i+1
        return ct