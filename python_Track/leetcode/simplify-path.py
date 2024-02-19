class Solution:
    def simplifyPath(self, path: str) -> str:
        all_dir = path.split('/')
        stack = []
        for i in all_dir:
            if len(i) and i == "..":
                if len(stack):
                    stack.pop()
            elif len(i) and i != '.':
                stack.append(i)
        return "/"+"/".join(stack)

        