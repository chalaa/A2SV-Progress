class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_solution(s: str, answer:str,k:int):
            i=j=_max=ct=pt = 0
            ind = []
            while j  < len(answer):
                if answer[j] == s:
                    ind.append(j+1)
                    ct+=1
                    if ct > k:
                        i = ind[pt]
                        pt += 1
                        ct -= 1
                _max = max(_max,(j-i+1))
                j+=1
            return _max

        return max(max_solution("T",answerKey,k),max_solution("F",answerKey,k))