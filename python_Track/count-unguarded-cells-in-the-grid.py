class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        uni_wall = set()
        uni_guard = set()
        visited = set()
        for i in walls:
            uni_wall.add(tuple(i))
        for i in guards:
            uni_guard.add(tuple(i))
        for point in guards:
            i,j = point
            while i > 0 and (i-1,j) not in uni_wall and (i-1,j) not in uni_guard:
                if (i-1,j) not in visited:
                    visited.add((i-1,j))
                i-=1

            i,j = point
            while i < m-1 and(i+1,j) not in uni_wall and (i+1,j) not in uni_guard:
                if (i+1,j) not in visited:
                    visited.add((i+1,j))
                i+=1

            i,j = point
            while j >0  and(i,j-1) not in uni_wall and (i,j-1) not in uni_guard:
                if (i,j-1) not in visited:
                    visited.add((i,j-1))
                j-=1

            i,j = point
            while j < n-1 and (i,j+1) not in uni_wall and (i,j+1) not in uni_guard:
                if (i,j+1) not in visited:
                    visited.add((i,j+1))
                j+=1

        print(uni_guard)
        return (n*m) - len(uni_guard) - len(uni_wall) -len(visited)
        