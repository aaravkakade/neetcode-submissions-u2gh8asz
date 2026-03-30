class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        "zxyzxyz"
        l = 0
        iterate through with r adding each to set

        while s[r] in set
        l + 1

        '''

        l = 0
        seen = set()

        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        
            res = max(res, r - l + 1)
        return res




            

