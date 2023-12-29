class Bitset:

    def __init__(self, size: int):
        self.tot = size
        self.sm = 0
        self.bitSet0 = ['0'] * size
        self.bitSet1 = ['1'] * size
        self.bitSet = self.bitSet0
        self.ct = 0

    def fix(self, idx: int) -> None:
        if self.bitSet[idx] == "0":
            self.sm += 1
        if self.ct % 2:
            self.bitSet0[idx] = '0'
            self.bitSet1[idx] = '1'
        else:
            self.bitSet0[idx] = '1'
            self.bitSet1[idx] = '0'

    def unfix(self, idx: int) -> None:
        if self.bitSet[idx] == "1":
            self.sm -= 1
        if self.ct % 2:
            self.bitSet0[idx] = '1'
            self.bitSet1[idx] = '0'
        else:
            self.bitSet0[idx] = '0'
            self.bitSet1[idx] = '1'

    def flip(self) -> None:
        self.ct +=1
        if self.ct % 2:
            self.bitSet = self.bitSet1
        else:
            self.bitSet = self.bitSet0
        self.sm = self.tot - self.sm

    def all(self) -> bool:
        return self.sm == self.tot

    def one(self) -> bool:
        return self.sm >= 1

    def count(self) -> int:
        return self.sm

    def toString(self) -> str:
        return "".join(self.bitSet)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()