class Solution:
    def isPalindrome(self, s: str) -> bool:
        # base case
        if (len(s) <= 1): return True
        s2 = ''
        for char in s:
            if char.isalnum():
                s2 += char
        s2 = s2.lower()
        # check if palindrome
        for i in range(len(s2) // 2):
            if (s2[i] != s2[len(s2) - i - 1]):
                return False
        
        return True