class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    x = stack.pop()
                    stack.pop()
                    stack.append(2*x)
                while len(stack) > 1 and stack [-1] != '(' and stack[-2] != '(':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x+y)
            i+=1
        return stack[-1]