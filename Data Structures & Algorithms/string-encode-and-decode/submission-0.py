class Solution:

    def encode(self, strs: List[str]) -> str:
        full_string = ""
        for i in range(len(strs)):
            length = len(strs[i])
            add_string = f"{length}#{strs[i]}"
            full_string += add_string
        return full_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            that_index = s.find("#", i)
            start = that_index + 1
            length = int(s[i:that_index])
            result.append(s[start:start+length])
            i = start + length
        return result
            
            

