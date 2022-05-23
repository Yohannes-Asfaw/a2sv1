class Solution:
    def countVowels(self, word: str) -> int:
        c, l = 0, len(word)
        d = {'a':1, 'e':1,'i':1,'o':1,'u':1}
        for i in range(l):
                if word[i] in d:
                    c += (l-i)*(i+1)
        return c
