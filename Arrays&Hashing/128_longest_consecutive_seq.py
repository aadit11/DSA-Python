"""
    We use a hashset to solve this problem. First we convert the list to a set to remove duplicates.
    Then we iterate through the set and check if the current number - 1 is not in the set.
    If it is not, we start a streak from the current number.
    Then we check if the current number + 1 is in the set.
    If it is, we increment the streak and the current number.
    Finally we return the longest streak.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    streak+=1
                    current+=1
                longest = max(longest,streak)

        return longest

