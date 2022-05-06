    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        j = 0
        res = 0
        for i in range(len(fruits)):
            basket[fruits[i]] += 1
            while len(basket) > 2:
                basket[fruits[j]] -= 1
                j += 1
                if basket[fruits[j - 1]] == 0:
                    del basket[fruits[j - 1]]
            res = max(res, i - j + 1)
        return res
