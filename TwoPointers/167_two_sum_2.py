"""
    We use two pointers to solve this problem. We start at the beginning and end of the list.
    We check if the sum of the two numbers is equal to the target.
    If it is, we return the indices of the two numbers.
    If it is not, we check if the sum is less than the target.
    If it is, we move the left pointer to the right.
    If it is not, we move the right pointer to the left.
"""



class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s < target:
                l +=1
            else:
                r-=1