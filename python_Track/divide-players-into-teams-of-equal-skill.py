class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2 !=0:
            return -1
        skill.sort()
        i=0
        j=len(skill)-1
        total_skill = skill[i]+skill[j]
        ans = 0
        while i<j:
            if skill[i]+skill[j] != total_skill:
                return -1
            else:
                ans+=(skill[i]*skill[j])
                i+=1
                j-=1
        return ans