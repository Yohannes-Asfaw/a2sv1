 def sortSentence(self, s: str) -> str:
        z = s.split()
        x = []
        k = ""
        for i in range(len(z)):
            x.append(0)
        for i in range(len(z)):
            m = int(z[i][-1])
            x[m - 1] = z[i][:-1]
        for i in range(len(z)):
            if i != len(z) - 1:
                k += x[i] + " "
            else:
                k += x[i]
        return k
