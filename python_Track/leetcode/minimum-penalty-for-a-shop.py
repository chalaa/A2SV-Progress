class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_arr = [0]
        n_arr = [0]
        for i in customers:
            if i == "Y":
                y_arr.append(1)
                n_arr.append(0)
            else:
                y_arr.append(0)
                n_arr.append(1)
        for i in range(1,len(y_arr)):
            y_arr[i] += y_arr[i-1]
            n_arr[i] += n_arr[i-1]

        min_pen = float('inf')
        min_ind = 0

        for i in range(len(y_arr)):
            x = y_arr[-1] - y_arr[i] +  n_arr[i]
            if x < min_pen:
                min_pen = x
                min_ind = i
        return min_ind
