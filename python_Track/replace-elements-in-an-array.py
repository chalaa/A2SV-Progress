class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        print(dic)
        for i in operations:
            ind = dic[i[0]]
            nums[ind] = i[1]
            dic[i[1]] = ind
            del(dic[i[0]])
        return nums
        