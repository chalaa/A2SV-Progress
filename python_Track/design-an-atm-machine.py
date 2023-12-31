class ATM:

    def __init__(self):
        self.total = {
            20 : 0,
            50 : 0,
            100 : 0,
            200 : 0,
            500 : 0
        }
        self.note = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.total[self.note[i]] += banknotesCount[i]

            
    def withdraw(self, amount: int) -> List[int]:
        ans = []
        for i in range(4,-1,-1):
            x = amount//self.note[i]
            if x > 0:
                if x <= self.total[self.note[i]]:
                    amount = amount - (self.note[i] * x)
                    self.total[self.note[i]] -= x
                    ans.append(x)
                else:
                    amount = amount - (self.note[i] * self.total[self.note[i]])
                    ans.append(self.total[self.note[i]])
                    self.total[self.note[i]] -= self.total[self.note[i]]
            else:
                ans.append(0)
        ans.reverse()
        if amount == 0:
            return ans
        else:
            for i in range(5):
                self.total[self.note[i]] += ans[i]
        return [-1]



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)