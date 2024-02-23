class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = Counter(senate)
        queue = deque()
        BR = BD =0
        # for i in senate:
        #     if i == "R":
        #         if BR == 0:
        #             queue.append(i)
        #             BD += 1
        #             counter['D'] -= 1
        #             if counter['D'] <= 0:
        #                 del(counter['D'])
        #                 return "Radiant"
        #         else:
        #             BR -= 1
        #     else:
        #         if BD == 0:
        #             queue.append(i)
        #             BR += 1
        #             counter['R'] -= 1
        #             if counter['R'] <= 0:
        #                 del(counter['R'])
        #                 return "Dire"
        #         else:
        #             BD -= 1
        if len(counter) == 1:
            if 'R' in counter:
                return 'Radiant'
            return "Dire"
        queue.extend(senate)
      
        while len(counter) > 1:
            i = queue.popleft()
            if i == "R":
                if BR == 0:
                    queue.append(i)
                    BD += 1
                    counter['D'] -= 1
                    if counter['D'] <= 0:
                        del(counter['D'])
                        return "Radiant"
                else:
                    BR -= 1
            else:
                if BD == 0:
                    queue.append(i)
                    BR += 1
                    counter['R'] -= 1
                    if counter['R'] <= 0:
                        del(counter['R'])
                        return "Dire"
                else:
                    BD -= 1



