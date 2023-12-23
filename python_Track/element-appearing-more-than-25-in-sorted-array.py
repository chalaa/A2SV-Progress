class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
            if dic[i] > len(arr)//4:
                return i