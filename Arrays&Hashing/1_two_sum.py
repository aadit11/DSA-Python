"""
    We use a hashmap to solve this problem. First we iterate through the list and add the number and its index to the map.
    Then we iterate through the list again and check if the target - the current number is in the map. If it is, we return the indices
    of the two numbers.
    If not, we add the number and its index to the map.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in map and map[val] != i:
                return [i,map[val]]

        return []
