class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr) - 1
        while i+1 < len(arr) and arr[i] < arr[i+1]:
            i+=1
        while j>0 and arr[j-1] > arr[j]:
            j-=1
        return (i > 0 and j < len(arr)-1 and i == j)
        