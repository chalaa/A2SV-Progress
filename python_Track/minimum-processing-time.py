class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        _max = 0
        j = 0
        for i in range(3,len(tasks),4):
            _max = max(_max,(tasks[i]+processorTime[j]))
            j+=1
        return _max