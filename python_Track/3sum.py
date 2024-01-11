class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        st=set()
        for i in range(len(nums)):
            k= len(nums)-1
            j=i+1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    st.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]<abs(nums[i]):
                    j+=1
                else:
                    k-=1
        return list(st)

