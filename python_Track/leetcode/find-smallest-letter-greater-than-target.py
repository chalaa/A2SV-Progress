class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = bisect_right(letters,target)
        return letters[x] if x < len(letters) else letters[0]