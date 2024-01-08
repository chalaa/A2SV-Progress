class Robot:

    def __init__(self, width: int, height: int):
        self.matrix = [height-1,width-1]
        self.pos = [0,0]
        self.direction = "East"

    def step(self, num: int) -> None:
        num = num % (2 * (self.matrix[0] + self.matrix[1]))
        if num == 0 and self.pos == [0, 0] and self.direction == "East":
            self.direction = "South"
        if num == 0 and self.pos == [self.matrix[0], 0] and self.direction == "South":
            self.direction = "West"
        if num == 0 and self.pos == self.matrix and self.direction == "West":
            self.direction = "North"
        if num == 0 and self.pos == [0, self.matrix[1]] and self.direction == "North":
            self.direction = "East"
        while num > 0:
            if self.direction =="East":
                n = self.matrix[1] - self.pos[1]
                if num <= n:
                    self.pos[1] += num
                    num = 0
                else:
                    self.pos[1] += n
                    num -= n
                    self.direction = "North"
            elif self.direction =="North":
                n = self.matrix[0] - self.pos[0]
                if num <= n:
                    self.pos[0] += num
                    num = 0
                else:
                    self.pos[0] += n
                    num -= n
                    self.direction = "West"
            elif self.direction =="West":
                n = self.pos[1]
                if num <= n:
                    self.pos[1] -= num
                    num = 0
                else:
                    self.pos[1] -= n
                    num -= n
                    self.direction = "South"
            elif self.direction =="South":
                n = self.pos[0] 
                if num <= n:
                    self.pos[0] -= num
                    num = 0
                else:
                    self.pos[0] -= n
                    num -= n
                    self.direction = "East"
    def getPos(self) -> List[int]:
        return reversed(self.pos)

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()