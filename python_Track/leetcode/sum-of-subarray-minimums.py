class Solution:
    # added
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        stack = []

        ## find the index of the next smallest to the left of the array
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        right = [n] * n
        stack = [] 

        ## find the index of the next smallest to the left of the array
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 
        ans =  0
        ## find the product of of the subarray arr[i] 
        ## is minimum (i - left[i]) * (right[i] - i) * arr[i]
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i) * arr[i]
            ans%=mod
        # ans = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return ans 