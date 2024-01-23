class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = defaultdict(int)
        i = j = 0
        _max = 0
        while j < len(fruits):
            fruit[fruits[j]] += 1
            while len(fruit.keys()) > 2:
                fruit[fruits[i]] -= 1
                if fruit[fruits[i]] == 0:
                    del(fruit[fruits[i]])
                i +=1
            _max = max(_max,j-i+1)
            j += 1
        return _max