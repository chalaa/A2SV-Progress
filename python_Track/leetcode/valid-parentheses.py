class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if len(stack)==0 or i in '[({':
                stack.append(i)
            else:
                if dic[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack