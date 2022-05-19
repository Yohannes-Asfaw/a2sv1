    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        if m==m[::-1]:
            return True
        else:
            return False
