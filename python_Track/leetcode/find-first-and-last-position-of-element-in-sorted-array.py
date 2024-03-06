class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        def search(left,right):
            if left>right:
                return
            mid = left + (right-left)//2
            if nums[mid] > target:
                search(left,mid-1)
            elif nums[mid] < target:
                search(mid+1,right)
            else:
                if ans[0] == -1:
                    ans[0] = mid
                else:
                    ans[0] = min(mid,ans[0])
                ans[1] = max(ans[1],mid)
                search(left,mid-1)
                search(mid+1,right)
        search(0,len(nums)-1)
        return ans