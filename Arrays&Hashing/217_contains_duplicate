"""
    We use a hashset to solve this problem. First we iterate through the list and add the number to the set.
    Then we iterate through the list again and check if the number is in the set. If it is, we return True.
    If not, we add the number to the set.
    If we finish the loop without finding any duplicates, we return False.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()
        for i in range(len(nums)):
            if nums[i] in dup:
                return True
            else:
                dup.add(nums[i])
        return False
            

        
        