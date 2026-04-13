"""
For each index in the string, treat it as the center of a palindrome.
Use two pointers and expand outward while characters match.
Do this for both odd and even length centers, and track the longest substring found.
"""




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s

        start = 0
        end = 0
        n = len(s)

        for i in range(n): 
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > end - start:
                    start = left
                    end = right
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > end - start:
                    start = left
                    end = right
                left -= 1
                right += 1
        
        return s[start:end + 1] 

            
        