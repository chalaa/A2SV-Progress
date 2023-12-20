class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        answer = ""
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return answer
            answer += strs[0][i]
        return answer
        