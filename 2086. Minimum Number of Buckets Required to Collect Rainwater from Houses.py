    def minimumBuckets(self, street: str) -> int:
        if 'HHH' in street or street[:2]=='HH' or street[-2:]=='HH' or street[:2]=='H': 
            return -1
        a=street.count('H')
        b=street.count('H.H')
        return a-b
