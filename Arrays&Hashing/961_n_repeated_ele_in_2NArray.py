"""
    We use a hashmap to solve this problem. First we iterate through the list and add the number and its frequency to the map.
    Then we iterate through the list again and check if the frequency of the number is equal to the length of the list divided by 2.
    If it is, we return the number.
"""


class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)//2
        freq = {}
        res = 0
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            if freq.get(i) == length:
                res = i

        return res

        