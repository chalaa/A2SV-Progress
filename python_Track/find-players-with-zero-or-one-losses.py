class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        loss = []
        for i in matches:
            win.add(i[0])
            loss.append(i[1])
        loss = Counter(loss)
        all_winner = []
        all_losser = []
        for i in win:
            if i not in loss:
                all_winner.append(i)
        for k,v in loss.items():
            if v == 1:
                all_losser.append(k)
        return [sorted(all_winner), sorted(all_losser)]

        