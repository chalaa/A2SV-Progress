class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ###approche 1
        ans = 0
        n = len(costs)//2
        a = 0
        b = 0
        arr = []
        ## create an array that store the absolute difference
        for i in costs:
            arr.append((abs(i[0]-i[1]),i[0],i[1]))
        #sort the array
        arr.sort(reverse = True)


        for i in arr:
            if a < n and b < n:
                x = min(i[1],i[-1])
                if x == i[1]:
                    a+=1
                else:
                    b+=1
            elif a < n:
                x = i[1]
                a+=1
            else:
                x = i[-1]
                b+=1
            ans += x
        return ans
        
        # ### approche 2

        # costs.sort(key = lambda x : x[0] - x[1])

        # n = len(costs) // 2
        # ans = 0
        # for i in range(n):
        #     ans += costs[i][0] + costs[i+n][1]
        
        # return ans