"""
    We use two pointers to solve this problem. We start at the beginning and end of the list.
    We check if the height of the left pointer is less than the height of the right pointer.
    If it is, we check if the height of the left pointer is greater than or equal to the left max.
    If it is, we update the left max.
    If it is not, we add the difference between the left max and the height of the left pointer to the water.
    We then move the left pointer to the right.
    If the height of the right pointer is greater than or equal to the right max, we update the right max.
    If it is not, we add the difference between the right max and the height of the right pointer to the water.
    We then move the right pointer to the left.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height or len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] 
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water       