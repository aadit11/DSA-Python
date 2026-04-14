"""
    We use a stack to solve this problem. We iterate through the string and add the characters to the stack.
    If the character is a closing bracket, we check if the stack is empty or the top of the stack is not the corresponding opening bracket.
    If it is, we return False.
    If it is not, we pop the top of the stack.
    If we finish the loop without finding any characters that are not the same, we return True.
"""




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


        
        