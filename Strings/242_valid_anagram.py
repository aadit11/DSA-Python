"""
    We use a hashmap to solve this problem. First we iterate through the first string and add the character and its frequency to the map.
    Then we iterate through the second string and check if the character is in the map. If it is, we decrement the frequency of the character.
    If not, we return False.
    If we finish the loop without finding any characters that are not in the map and the map is empty, we return True.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] = freq.get(ch) - 1
            if freq[ch] == 0:
                del freq[ch]
        return True

        

    