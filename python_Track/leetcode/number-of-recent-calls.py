class RecentCounter:

    def __init__(self):
        self.qe = []
        self.j = 0

    def ping(self, t: int) -> int:
        self.qe.append(t)
        dif = t - 3000
        while dif > self.qe[self.j]:
            if self.j < len(self.qe):
                self.j+=1
            else:
                break
        return len(self.qe) - self.j

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)