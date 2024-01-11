class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        graph = defaultdict(list)
        for i in range(len(nums)):
            x = (i+ nums[i]) % len(nums)
            graph[i].append(x)
        
        print(graph)
        for k in graph:
            visited = set()
            pos = 0
            neg = 0
            stack = [k]
            while len(stack):
                x = stack.pop()
                if x in visited:
                    if pos == 0 or neg == 0:
                        return True
                    else:
                        break
                visited.add(x)
                if nums[x] > 0:
                    pos += 1
                if nums[x] < 0:
                    neg += 1 
                if not x in graph[x]:
                    stack.extend(graph[x])
        
        return False

