class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0,20:0}
        for i in bills:
            if i == 5:
                dic[i] +=1
            elif i == 10:
                if dic[5] >= 1:
                    dic[5] -= 1
                    dic[i] += 1
                else:
                    return False
            else:
                if dic[10] >= 1:
                    dic[10] -= 1
                    if dic[5] >= 1:
                        dic[5] -= 1
                        dic[i] += 1
                    else:
                        return False
                elif dic[5]>=3:
                    dic[5] -= 3
                    dic[i] += 1
                else:
                    return False
        return True