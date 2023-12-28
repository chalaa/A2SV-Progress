class OrderedStream:

    def __init__(self, n: int):
        self.ans = [None]*n
        self.pt = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans[idKey - 1] = value
        res = []

        while self.pt < len(self.ans) and self.ans[self.pt] != None:
            res.append(self.ans[self.pt])
            self.pt += 1
            
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)