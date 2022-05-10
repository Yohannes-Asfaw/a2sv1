    def isPalindrome(self, s: str) -> bool:
        m = []
        for i in s:
            if 97 <= ord(i) <= 122:
                m.append(i)
            elif 65 <= ord(i) <= 90:
                m.append(chr(ord(i) + 32))
            elif 48 <= ord(i) <= 57:
                m.append(chr(ord(i) + 32))
        if m == m[::-1]:
            return True
        else:
            return False
