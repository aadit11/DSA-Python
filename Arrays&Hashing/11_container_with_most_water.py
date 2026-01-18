"""
  We use two pointers to solve this problem. We start at the beginning and end of the list.
  We check the area of the two pointers and move the pointer that is smaller to the center.
  As we move the pointers, we check if the area is greater than the maximum area.
  If it is, we update the maximum area.
  If the two pointers are equal, we move both pointers to the center.
  We return the maximum area.
"""




class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxi = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = h * w
            maxi = max(maxi,area)
            if(height[left] < height[right]):
                left+=1
            elif(height[left] > height[right]):
                right-=1
            else:
                left+=1
                right-=1
        
        return maxi

            
            
