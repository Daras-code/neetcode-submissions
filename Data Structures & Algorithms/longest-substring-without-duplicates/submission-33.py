class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
                
            elif seen[char] >= start: 
                start = seen[char] + 1
                seen[char] = i
            max_length = max(max_length, i-start+1)
            seen[char] = i

        return max_length
