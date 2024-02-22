class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [1]
        last = self.getRow(rowIndex-1)
        for i in range(len(last)-1):
            res.append(last[i]+last[i+1])
        res.append(1)
        return res