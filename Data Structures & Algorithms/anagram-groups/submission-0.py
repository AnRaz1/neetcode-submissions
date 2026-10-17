class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in groups:
                groups[sortedString].append(string)
            else:
                groups[sortedString] = [string]
        result = list(groups.values())
        return result
