class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ty = []
        i = 0
        j = 0
        while i < len(name) and j <len(typed):
            n = i
            m = j
            if name[i] != typed[j]:
                return False
            while n < len(name) and name[i] == name[n]:
                n += 1
            while m < len(typed) and typed[j] == typed[m]:
                m += 1
            if (m - j) < (n -i):
                return False
            j = m
            i = n
        if i == len(name) and j == len(typed):
            return True
        return False
            
            