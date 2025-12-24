
"""
    We use a hashmap to solve this problem. First we sort all the words in the list using sorted() as its create 
    a new list and keeps the original one unchanged.
    In the hashmap, the key is the sorted word and the value are the list of words that are anagarms. It will be appended 
    to the same key if the sorted word is the same otherwise a new key will be created.
    Then we just return the values of the map as they are the set of anagrams.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in map:
                map[sorted_word] = []
            map[sorted_word].append(word)

        return list(map.values())


        