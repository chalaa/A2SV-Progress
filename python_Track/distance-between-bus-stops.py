class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int: 
        x = min(start,destination)
        y = max(start,destination)
        ck = 0
        ant = 0
        print(start,destination)
        n = len(distance)
        distance += distance
        for i in range(x, y):
            ck += distance[i]
        for i in range(x+n-1, y-1, -1):
            ant += distance[i]
        return min(ck,ant)