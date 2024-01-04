class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ls = []
        lst = arr
        while(len(lst)> 0):
            ind = lst.index(max(lst))
            if(ind == 0):
                ls.append(len(lst))
                lst.reverse()
                lst.pop()
            elif(ind == len(lst)-1):
                lst.pop()
            else:
                ls.append(ind+1)
                lst = lst[ind::-1]+lst[ind+1::]
        return ls