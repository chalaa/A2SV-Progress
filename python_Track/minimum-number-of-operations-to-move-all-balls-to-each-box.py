class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ct = [i for i in range(len(boxes)) if boxes[i] == '1']
        ans = []
        for i in range(len(boxes)):
            sm = 0
            for j in ct:
                sm += abs(j-i)
            ans.append(sm)
        return ans
        