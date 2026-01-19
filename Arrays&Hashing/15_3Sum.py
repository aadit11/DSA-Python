"""
    We use two pointers to solve this problem. We start at the beginning and end of the list.
    We sort the list to make it easier to find the three numbers.
    We then iterate through the list and use two pointers to find the three numbers.
    We check if the sum of the three numbers is equal to the target.
    If it is, we add the three numbers to the result list.
    If it is not, we check if the sum is less than the target.
    If it is, we move the left pointer to the right.
    If it is not, we move the right pointer to the left.
    We continue to do this until we find the three numbers.
    We return the result list.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums) 
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
            

        
        