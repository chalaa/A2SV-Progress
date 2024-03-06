class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ### approach 1
        # x = bisect_right(letters,target)
        # return letters[x] if x < len(letters) else letters[0]
        ### approach 2
        def bisect_right(arr,target):
            left = 0
            right = len(letters)-1
            while left <= right:
                mid = left + ceil((right-left)/2)
                if arr[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            if left == len(arr):
                return 0
            return left
        ind = bisect_right(letters,target)
        return letters[ind]