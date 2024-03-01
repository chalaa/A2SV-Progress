class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _map = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        ans = []
        def generate(arr,ind):
            if arr and len(arr) == len(digits):
                ans.append("".join(arr[:]))
            if ind >= len(digits):
                return
            for i in _map[digits[ind]]:
                arr.append(i)
                generate(arr,ind+1)
                arr.pop()
        generate([],0)
        return ans
        