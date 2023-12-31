class FrequencyTracker:

    def __init__(self):
        self.dic = defaultdict(int)
        self.feq = defaultdict(int)

    def add(self, number: int) -> None:
        x = self.dic[number]
        self.dic[number] += 1
        self.feq[x] -= 1
        self.feq[self.dic[number]] += 1
        

    def deleteOne(self, number: int) -> None:
        if self.dic[number] >= 1:
            x = self.dic[number]
            self.dic[number] -= 1
            self.feq[x] -= 1
            self.feq[self.dic[number]] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        if self.feq[frequency]:
            print(self.feq)
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)