class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## concatinate the list of number in to string
        s = "".join(map(str, digits))

        ## cast s to int and add 1 and cast it to string
        s = str(int(s) + 1)

        return list(map(int, list(s)))