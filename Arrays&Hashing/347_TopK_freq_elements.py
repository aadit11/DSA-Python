"""
    We use a hashmap to solve this problem. First we iterate through the list and add the number and its frequency to the map.
    Then we sort the map by the frequency of the numbers in descending order.
    Finally we return the first k numbers from the sorted map.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        sorted_nums = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
        return sorted_nums[:k]