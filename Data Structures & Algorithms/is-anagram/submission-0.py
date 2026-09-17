class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = list(t)
        for char in s:
            if char in temp:
                temp.remove(char)
        if temp == []:
            return True
        else:
            return False

            

        