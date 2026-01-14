"""
    We solve this problem by iterating through the list and checking if the number has four divisors.
    We use a nested loop to check if the number has four divisors.
    We use the math library to calculate the square root of the number.
    And we use a counter to check if the number has four divisors.
    If the number has four divisors, we add the number to the sum.
    If the number does not have four divisors, we continue to the next number.
    Finally we return the sum.
"""


import math
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0

        for i in nums:
            count = 0
            in_sum = 0

            for div in range(1,int(math.sqrt(i)) + 1):
                if i % div == 0:
                    other = i // div

                    if div == other:
                        count += 1
                        in_sum += div
                    else:
                        count += 2
                        in_sum += div + other
                    
                    if count > 4:
                        break
            
            if count == 4:
                sum += in_sum

        return sum
            
        