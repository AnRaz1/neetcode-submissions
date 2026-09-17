class Solution:
    def isValid(self, s: str) -> bool:
        # base case: odd number of brackets
        if (len(s) % 2 != 0): return False
        stack = []
        c_to_s = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for i in range(len(s)):
            if (s[i] in c_to_s):
                if stack and (stack[-1] == c_to_s[s[i]]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False # valid if stack is empty
