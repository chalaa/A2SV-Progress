class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        doubles = {x for i, x in enumerate(fronts) if backs[i]==x}
        mn = float("infinity")
        for i in (fronts + backs):
            if i not in doubles:
                mn = min(mn,i)
        if mn != float("infinity"):
            return mn
        return 0
            


        