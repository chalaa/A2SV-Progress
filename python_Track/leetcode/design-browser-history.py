class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.pt = 0

    def visit(self, url: str) -> None:
        j = len(self.arr) - 1
        while j > self.pt:
            self.arr.pop()
            j-=1
        self.arr.append(url)
        self.pt = len(self.arr) - 1
    def back(self, steps: int) -> str:
        self.pt -= steps
        if self.pt < 0:
            self.pt = 0
        return self.arr[self.pt]

    def forward(self, steps: int) -> str:
        self.pt += steps
        if self.pt >= len(self.arr):
            self.pt = len(self.arr)-1
        return self.arr[self.pt]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)