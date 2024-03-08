class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ind = min(bisect_left(arr,x),len(arr)-1)
        if arr[ind] == x:
            ans = [arr[ind]]
        else:
            _left = abs(x-arr[ind])
            _right = abs(x-arr[ind-1])
            if _left >= _right:
                ind -= 1 
            ans = [arr[ind]]
        left, right = ind-1,ind+1
        for i in range(k-1):
            if left >= 0 and right < len(arr):
                _left = x-arr[left]
                _right = arr[right]-x
                if _left <= _right:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            elif left >= 0:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        return sorted(ans)
