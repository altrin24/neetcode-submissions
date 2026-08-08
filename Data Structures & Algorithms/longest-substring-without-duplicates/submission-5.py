class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        left = 0
        max_count = 0

        for right,ch in enumerate(s):

            if ch in mp and mp[ch] >= left:
                left = mp[ch] + 1

            mp[ch] = right

            count = right - left + 1
            max_count = max(count,max_count)


        return max_count        
