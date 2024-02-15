class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for i in counter:
            ans += (i+1) * ceil(counter[i]/(i+1))
        return ans
        