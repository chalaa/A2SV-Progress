class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        ls1 =[]
        ls2=[]
        dic = {}
        for i in points:
            a= (i[0]**2)+(i[1]**2)
            ls1.append(a)
            ls2.append(i)
        for i in range(k):
            s=ls1.index(min(ls1))
            ls.append(ls2[s])
            ls1.pop(s)
            ls2.pop(s)
        return ls