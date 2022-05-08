
    def lengthOfLongestSubstring(self, s: str) -> int:
        londstr = collections.defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            londstr[s[i]] += 1
            while londstr[s[i]]>1:
                londstr[s[j]] -= 1
                j+=1
            res = max(res, i - j + 1)
        return res
