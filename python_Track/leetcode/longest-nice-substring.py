class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def divide(current_string,string_set):
            if len(current_string) == 0:
                return ""

            for i in range(len(current_string)):
                if current_string[i].upper() not in string_set or current_string[i].lower() not in string_set:
                    x = current_string[:i]
                    left = divide(x,set(x))
                    y = current_string[i+1:]
                    right = divide(y,set(y))

                    if len(left) < len(right):
                        return right
                    return left
            return current_string
        
        return divide(s,set(s))