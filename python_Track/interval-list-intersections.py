class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(firstList):
            j = 0
            while j < len(secondList):
                if (secondList[j][0] <= firstList[i][0] <= secondList[j][1]) or firstList[i][0] <= secondList[j][0] <= firstList[i][1]:
                    ls = [max(firstList[i][0],secondList[j][0]), min(firstList[i][1],secondList[j][1])]
                    ans.append(ls)
                j+=1
            i += 1
        return ans