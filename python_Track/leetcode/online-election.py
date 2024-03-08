class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        freq = defaultdict(int)
        prev = persons[0]
        for i in range(len(persons)):
            freq[persons[i]] += 1
            if freq[persons[i]] >= freq[prev]:
                prev = persons[i]
            self.persons[i] = prev

    def bisect_right(self,arr,target):
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = left + (right-left)//2
            if arr[mid] <= target:
                left = mid+1
            else:
                right = mid -1
        return left
    def q(self, t: int) -> int:
        return self.persons[bisect_right(self.times,t)-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)