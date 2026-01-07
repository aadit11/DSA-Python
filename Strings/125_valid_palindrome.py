"""
    We use two pointers to solve this problem. We start at the beginning and end of the string.
    We check if the characters are alphanumeric. If they are not, we skip them.
    If they are, we check if they are the same. If they are not, we return False.
    If they are, we continue to the next characters.
    If we finish the loop without finding any characters that are not the same, we return True.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False


            left += 1
            right -= 1
        
        return True




        

        