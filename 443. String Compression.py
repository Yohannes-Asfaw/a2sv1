   def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        an = []
        i, j = 0, 1
        while j <= len(chars):
            if j == len(chars):
                an.append(chars[i])
                if j-i > 1:
                    for m in str(j-i):
                        an.append(m)
                break
            elif chars[i] != chars[j]:
                an.append(chars[i])
                if j-i > 1:
                    for m in str(j-i):
                        an.append(m)
                i = j
                j += 1
            else:
                j += 1
        chars.clear()
        for i in range(len(an)):
            chars.append(an[i])
        return len(chars)
    
    
    
    
     
