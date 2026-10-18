class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            freqs = "".join(str(self.getFreq(string)))
            if freqs in groups:
                groups[freqs].append(string)
            else:
                groups[freqs] = [string]
        result = list(groups.values())
        return result

    def getFreq(self, string: str) -> List[int]:
        freqs = [0] * 26
        for char in string:
            if 'a' <= char <= 'z':
                freqs[ord(char) - ord('a')] += 1
        return freqs