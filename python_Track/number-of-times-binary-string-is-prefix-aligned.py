class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _sum = 0
        count = 0
        number = [0] * len(flips)
        for i in range(len(flips)):
            if number[i] == 1:
                _sum+=1
            flip = flips[i] - 1
            if number[flip] == 0:
                number[flip] = 1
                if flip <= i:
                    _sum += 1
            else:
                number[flip] = 0
                if flip <= i:
                    _sum -= 1
            if _sum == i+1:
                count += 1
        return count