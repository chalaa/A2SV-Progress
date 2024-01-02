class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            j = 0
            k = len(image[i])-1
            while j < k:
                image[i][j],image[i][k] = image[i][k],image[i][j]
                j+=1
                k-=1
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
        
        