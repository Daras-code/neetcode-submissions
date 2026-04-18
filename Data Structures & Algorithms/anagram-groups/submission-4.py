class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorteddict = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in sorteddict:
                sorteddict[key].append(s)
            else:
                sorteddict[key] = [s]
        return list(sorteddict.values())