class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])
        i = 0
        j = 0
        while i < n and j < m:
            ls = []
            a = i
            b = j
            while a < n and b > -1:
                ls.append(mat[a][b])
                a += 1
                b -= 1
            if (i+j) % 2 == 0:
                ls.reverse()
            if j < m-1:
                j+=1
            else:
                i+=1
            ans.extend(ls)
        return ans

