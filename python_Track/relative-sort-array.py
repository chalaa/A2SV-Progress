class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for i in arr2:
            for j in range(counter[i]):
                ans.append(i)
        not_f = sorted(set(arr1) - set(arr2))
        for i in not_f:
            for j in range(counter[i]):
                ans.append(i)
        return ans