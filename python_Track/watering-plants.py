class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 1
        tot = capacity
        for i in range(len(plants)):
            if plants[i] <= tot:
                if i != len(plants)-1:
                    ans+=1
                tot -= plants[i]
            else:
                ans+=(2*i)
                tot = capacity
                tot -= plants[i]
                if i != len(plants)-1:
                    ans+=1
        return ans

        