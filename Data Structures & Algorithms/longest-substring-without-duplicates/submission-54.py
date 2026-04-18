class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_length = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
    
            elif s[right] in seen:
                seen.remove(s[left])
                left += 1 
            max_length = max((right-left),max_length)
        return max_length
                