class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        l_t = max(target[0],0) - min(target[0],0) +  max(target[1],0) - min(target[1],0)
        for i in ghosts:
            if (max(target[0],i[0]) - min(target[0],i[0]) +  max(target[1],i[1]) - min(target[1],i[1])) <= l_t:
                return False
        return True